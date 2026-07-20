import time

# ---------------------------------------------------
# 동기방식
# ---------------------------------------------------
def sync_a():
    print("A 시작")
    time.sleep(2)
    print("A 끝")
    
def sync_b():
    print("B 시작")
    time.sleep(2)
    print("B 끝")
    
start = time.time()
sync_a()
sync_b()
end = time.time()
print(f"실행시간: {end-start:.2f}초")


# ---------------------------------------------------
# 비동기방식
# ---------------------------------------------------

import asyncio

# 동기방식
async def async_a():
    print("A 시작")
    await asyncio.sleep(2)
    print("A 끝")
    
async def async_b():
    print("B 시작")
    await asyncio.sleep(2)
    print("B 끝")

async def main():
    c1 = async_a()    # 코루틴 객체
    c2 = async_b()
    await asyncio.gather(c1, c2)
    
start = time.time()
asyncio.run(main())  # main 코루틴 객체
end = time.time()
print(f"실행시간: {end-start:.2f}초")