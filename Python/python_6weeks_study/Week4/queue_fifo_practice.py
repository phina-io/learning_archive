# 큐(Queue): 선입선출(FIFO)의 메커니즘

#---------------------------------------------
# 1. 큐의 정의와 효율적 구현
#---------------------------------------------

# FIFO(First In First Out): 먼저 들어온 요소가 먼저 나가는 공정한 처리 원칙
# Deque(Double Ended Queue): 양쪽 끝에서 삽입과 삭제가 모두


#---------------------------------------------
# 2.1 collections.deque를 이용한 큐
#---------------------------------------------
# 원형 구조에서 특정 순서의 요소를 반복적으로 제거하는 과정
from collections import deque

# 큐 생성
queue = deque()
print(f"초기 큐: {queue}")

# Enqueue 연산: 큐에 데이터 추가
queue.append(100)
queue.append(200)
queue.append(300)
print(f"데이터 Enqueue 후: {queue}")

# Dequeue 연산: 큐에서 데이터 꺼내기
# deque의 popleft() 메소드. 왼쪽 끝에서 제거
if queue:
    dequeued_element = queue.popleft()
    print(f"Dequeue된 데이터: {dequeued_element}")
    print(f"데이터 Dequeue 후: {queue}")

# 모든 데이터 Dequeue 하기
dequeued_element = queue.popleft()
print(f"Dequeue된 데이터: {dequeued_element}, 큐 상태: {queue}")
dequeued_element = queue.popleft()
print(f"Dequeue된 데이터: {dequeued_element}, 큐 상태: {queue}")

# 큐가 비었는지 확인
if not queue:
    print("큐가 비어있습니다")

#---------------------------------------------
# 2.2 오세푸스 문제와 회전(Circular Queue)
#---------------------------------------------
# 원형 구조에서 특정 순서의 요소를 반복적으로 제거하는 과정

def josephus_problem(N, K):
    # 1번부터 N번까지의 사람을 큐에 배치
    queue = deque(range(1, N + 1))
    
    print(f"총 사람수: {N}, 제거될 사람의 순서: {K} 요세푸스 문제 시작")
    print(f"초기 큐: {list(queue)}")
    
    while len(queue) > 1:
        # K -1명의 사람을 큐의 맨 앞에서 빼서 맨 뒤로 보냄
        for _ in range(K - 1):
            person = queue.popleft()
            queue.append(person)
        
        # K번째 사람을 큐에서 제거
        removed_person = queue.popleft()
        print(f"{removed_person}번 제거. 현재 큐: {list(queue)}")
    
    # 큐에 마지막으로 남은 한 명을 반환   
    return queue[0]

# 7명의 사람, 3번째 사람을 계속 제거
N_val = 7
K_val = 3
last_survivor = josephus_problem(N_val, K_val)
print(f"최종 생존자: {last_survivor}")


#---------------------------------------------
# 3. 프린터 대기열(Priority Simulation)
#---------------------------------------------
import time
import random

def printer_simulation(priorities, location):
    # (중요도, 초기 인덱스) 형태로 큐를 구성하여 위치 추적 가능하게 함
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    print_order = 0
    
    while queue:
        # 대기열의 가장 앞 문서를 꺼냄
        current = queue.popleft()
        
        # 현재 문서보다 중요도가 더 높은 문서가 대기열에 있는지 확인
        # any() 함수는 조건을 만족하는 요소가 하나라도 있으면 True 반환
        if any(current[0] < item[0] for item in queue):
            # 더 중요한 문서가 있다면 현재 문서를 맨 뒤로 다시 보냄(재순환)
            queue.append(current)
        else:
            # 출력 수행
            print_order += 1
            # 만약 방금 출력한 문서가 내가 요청한 위치의 문서라면 종료
            if current[1] == location:
                return print_order
            
print("--- 프린터 시뮬레이션 테스트 시작 ---")

# 문서 중요도: A, B, C, D / 추적 할 문서: C(인덱스 2)
res1 = printer_simulation([2, 1, 3, 2], 2)
print(f"테스트 1 결과: {res1} (기대값: 1)")

# 문서 중요도: 6개의 문서 중 인덱스 0번 문서가 몇 번째로 출력되는지 추적
res2 = printer_simulation([1, 1, 9, 1, 1, 1], 0)
print(f"테스트 2 결과: {res2} (기대값: 5)")

# 문서 중요도: 모든 중요도가 같을 때
res3 = printer_simulation([5, 5, 5, 5], 1)
print(f"테스트 3 결과: {res3} (기대값: 2)")