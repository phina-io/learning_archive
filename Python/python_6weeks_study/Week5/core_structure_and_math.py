# 기초 알고리즘 (Sort, Counter, Prime)

# 1. [정렬 & 카운터] 강력한 도구 활용

# 미션 1: 커스텀 정렬 (Lambda Sort)
# 인덱스 n번째 글자를 기준으로 오름차순 정렬, n번째 글자가 같으면 사전순으로 정렬

def string_sort(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

strings1 = ["sun", "bed", "car"]
print(f"인덱스 n번째 정렬: {string_sort(strings1, 1)}")

strings2 = ["abce", "abcd", "cdx"]
print(f"인덱스, 사전순 정렬: {string_sort(strings2, 1)}")


# 미션 2: 최빈값과 애너그램 (Counter)
# 최빈값과 에너그램인지 판별하기
from collections import Counter

# 최빈값
data = [1, 2, 2, 3, 3, 3]
counter = Counter(data)
most_frequent = counter.most_common(1)[0][0]
print(f"최빈값: {most_frequent}")


# 에너그램
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

s1 = "listen"
s2 = "silent"
print(f"에너그램 판별: {is_anagram(s1, s2)}")


# 2. [수학] 소수 판별 알고리즘

# 미션 3: 기본 소수 판별 (Primality Test)
# 정수 n이 주어졌을 때, 이 수가 소수(Prime Number)인지 판별

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"정수 17은 소수? {is_prime(17)}")
print(f"정수 20은 소수? {is_prime(20)}")


# 미션 4: 에라토스테네스의 체
# 자연수 n이 주어졌을 때, 1부터 n까지의 모든 소수의 개수

def get_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
                
    return [i for i, is_prime in enumerate(sieve) if is_prime]

result = get_primes(10)
count = len(result)
primes_str = ", ".join(map(str, result))

print(f"결과: {count} ({primes_str} 총 {count}개)")




