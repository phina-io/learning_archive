# LLM 응답 생성
import json
import redis

from llama_cpp import Llama


redis_client = redis.from_url(
    "redis://redis:6379", 
    decode_responses=True,
    socket_timeout=None,
)

llm = Llama(
    model_path="./models/Llama-3.2-1B-Instruct-Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=2,
    verbose=False,
    chat_format="llama-3",
)

SYSTEM_PROMPT = (
    "You are a concise assistant. "
    "Always reply in the same language as the user's input. "
    "Do not change the language. "
    "Do not mix languages."
)

# Worker는 동기식으로 작성한 이유
# Worker는 한번에 하나의 추론 작업만 하기 때문에
# 애초에 대기시간 발생하지 않음(I/O 작업이 아님)
def run():
    while True:
        # 1) 큐에서 작업을 Dequeue, brpop 요청이 올때까지 대기
        _, job = redis_client.brpop("inference_queue")
        job_dict = json.loads(job)
        
        user_input = job_dict["user_input"]
        
        # 2) Llama 응답 생성
        response = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content":user_input},
            ],
            max_tokens=256,
            temperature=0.7,
            stream=True
        )
        
        # 3) 채널로 응답 전송
        channel_id = job_dict["channel_id"]
        for chunk in response:
            token = chunk["choices"][0]["delta"].get("content")
            if token:
                redis_client.publish(channel_id, token)
        redis_client.publish(channel_id, "[DONE]")


# 직접 실행한 경우에만, run() 실행    
if __name__ == "__main__":
    run()