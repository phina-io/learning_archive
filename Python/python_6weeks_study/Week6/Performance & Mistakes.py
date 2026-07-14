# 1. [Performance] 효율성 최적화 훈련
# 미션 1: 리스트 vs 셋(Set) 검색 속도 비교
# 100만 개의 데이터가 있는 리스트와 셋을 만들고, 특정 값이 존재하는지 확인하는 in 연산의 시간을 비교
import time
large_range = range(1000000)
list = list(large_range)
set = set(large_range)

target = 999999

# list 시간측정
start = time.time()
_ = target in list
end = time.time()
print(f"리스트 검색 걸린 시간: {end - start:.5f}초")

# set 시간측정
start = time.time()
_ = target in set
end = time.time()
print(f"set 검색 걸린 시간: {end - start:.5f}초")


# 미션 2: 문자열 합치기 최적화
# 효율적인 방식(join)을 사용하는 함수
def efficient_concat(strings):
    return "".join(strings)

strings = ["Hello", " ", "World", "!"]
print(f"출력 결과: {efficient_concat(strings)}")


# 2. [Mistakes] 실수 방지와 방어적 코딩
# 미션 3: 얕은 복사의 함정 탈출
# 2차원 리스트 [[0]*3]*3으로 초기화했을 때 발생하는 문제를 올바른 2차원 리스트 초기화 코드로
bad = [[0] * 3] * 3
bad[0][0] = 9
print(f"잘못된 방법: {bad}")

good = [[0] * 3 for _ in range(3)]
good[0][0] = 9
print(f"올바른 방법: {good}")


# 미션 4: 리스트 순회 중 삭제 문제
# 정수 리스트에서 홀수 제거. 안전한 방법으로 구현.
numbers = [1, 2, 3, 4, 5]

safe_result = [num for num in numbers if num % 2 == 0]
print(f"컴프리헨션 결과: {safe_result}")

numbers_copy = [1, 2, 3, 4, 5]
for i in range(len(numbers_copy) -1, -1, -1):
    if numbers_copy[i] % 2 != 0:
        del numbers_copy[i]
print(f"역순 순회 삭제 결과: {numbers_copy}")
