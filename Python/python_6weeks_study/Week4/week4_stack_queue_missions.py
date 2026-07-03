# # 선형 자료구조 (Stack & Queue) 응용

# 1. [스택] LIFO 구조와 괄호 검사
# 미션 1: 문자열 뒤집기(Stack 활용)
def reverse_string(my_string):
    stack = []
    
    for char in my_string:
        stack.append(char)
    reverse_str = ""
    
    while stack:
        reverse_str += stack.pop()
    return reverse_str

print(reverse_string("Hello World"))


# 미션 2: 괄호 짝 맞추기(Valid Parentheses)
def is_valid_parentheses(s):
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        
        elif char == ")":
            if not stack:
                return False
            stack.pop()
            
    return not stack

s = [
    "(())()",
    "(()(",
    ")()(" 
]

for case in s:
    if is_valid_parentheses(case):
        print(f"{case} → True")
    else:
        print(f"{case} → False")


# 2. [큐] FIFO 구조와 시뮬레이션
# 미션 3: 요세푸스 문제(원형 큐)
from collections import deque

def josephus_problem(N, K):
    queue = deque(range(1, N + 1))
    result = []
    
    while queue:
        queue.rotate(-(K - 1))
        removed = queue.popleft()
        result.append(removed)
        
    return result

N_val = 7
K_val = 3
output = josephus_problem(N_val, K_val)
print(f"결과: {output}")


# 미션 4: 프린터 대기열 시뮬레이션
def printer_simulation(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    print_order = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[1] == location:
                return print_order

priorities1 = [2, 1, 3, 2]
location1 = 2
output1 = printer_simulation(priorities1, location1)
print(f"출력: {output1}")

priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0
output2 = printer_simulation(priorities2, location2)
print(f"출력: {output2}")