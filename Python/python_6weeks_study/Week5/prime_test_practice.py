# 정수론 기초: 효율적인 소수 판별(Primality Test)

def is_prime(n):
    # 0과 1은 소수가 아님
    if n < 2: 
        return False
    
    # 2부터 루트 n까지의 정수들에 대해 나누어 떨어지는지 확인
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"17은 소수인가? {is_prime(17)}")
print(f"20은 소수인가? {is_prime(20)}")


# 큰 숫자로 속도 차이 확인하기
import time

def is_prime_naive(n):
    # 0과 1은 소수가 아님
    if n < 2: 
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

large_prime = 2147483647

print("--- 소수 판별 속도 비교 테스트 ---")

# 비효율적인 방법
start = time.time()
is_prime_naive(large_prime)
end = time.time()
print(f"비효율적인 방법이 걸린 시간: {end - start:.5f}초")

# 효율적인 방법
start = time.time()
is_prime(large_prime)
end = time.time()
print(f"루트(0.5승)까지만 나누는 방법 걸린 시간: {end - start:.5f}초")


# 특정 범위 내의 소수 개수 세기
start_num = 1
end_num = 100
prime_list = []

for num in range(start_num, end_num + 1):
    if is_prime(num):
        prime_list.append(num)

print(f"1부터 100까지 소수의 개수: {len(prime_list)}개")
print(f"소수 목록: {prime_list}")