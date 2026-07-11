# 범위 내 소수 대량 탐색 (Eratosthenes' Sieve)
def get_prime_count(n):
    # 소수 여부를 저장할 리스트 생성(0~n까지, 초기화 True)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # 2부터 루트 n까지 순회하며 배수 제거
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n +1, i):
                sieve[j] = False
    return sum(sieve)

print(f"10까지의 소수 개수: {get_prime_count(10)}")


# 소수 목록 리스트
def get_prime_list(n):
    sieve = [True] * (n +1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n +1, i):
                sieve[j] = False
                
    # True 자리의 방 번호만 골라 리스트로 만들기
    # 리스트 컴프리헨션을 사용한 최적화 기법
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

print(f"30까지의 소수들: {get_prime_list(30)}")


# 구간 탐색
def get_prime_in_range(start, end):
    # 가장 큰 숫자인 end기준
    sieve = [True] * (end +1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(end**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end +1, i):
                sieve[j] = False
    
    # 위에 조건을 만족하는 것들중 원하는 범위(start, end)만 잘라서 가져오기
    range_primes = [i for i in range(start, end +1) if sieve[i]]
    return range_primes

print(f"50부터 80 사이의 소수: {get_prime_in_range(50, 80)}")


# 베르트랑 공준. n보다 크고 2n보다 작거나 같은 소수의 개수 구하기
def bertrand_postulate(n):
    # n부터 2n까지 검사해야 하므로 2*n
    limit= 2 * n
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[1]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
                
    # n보다 크고 2n보다 작거나 같은 범위의 소수만 카운트
    count = 0
    for i in range(n +1, limit + 1):
        if sieve[i]:
            count += 1
    return count
print(f"10보다 크고 20보다 작거나 같은 소수의 개수: {bertrand_postulate(10)}개")