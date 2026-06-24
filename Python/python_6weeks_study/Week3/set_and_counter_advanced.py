# SET
# 교집합 연산의 효율성
list_a = [1, 5, 2, 3]
list_b = [2, 3, 4, 5, 9]

set_a, set_b = set(list_a), set(list_b)

common_elements = set_a & set_b
result = sorted(list(common_elements))

print(f'공통 요소 확인: {result}')


# 데이터분석(Set 활용)
A_user = {'하늘', '하나', '바다', '태양'}
B_user = {'바다', '태양', '구름', '달빛'}

all_user = A_user | B_user
only_A = A_user - B_user

print(f'전체 이용자: {all_user}')
print(f'A만 이용자: {only_A}')


#-----------------------------------------------------------------------------
# 문자열 빈도수 계산기
# 딕셔너리 활용
fruits = ['apple', 'orange', 'apple', 'cherry', 'cherry', 'apple']

counts_dict = {}
for fruit in fruits:
    if fruit not in counts_dict:
        counts_dict[fruit] = 0 
    counts_dict[fruit] += 1
print(f'dict 사용 결과: {dict(counts_dict)}')


# collections.defaultdict
from collections import defaultdict

counts_defaultdict = defaultdict(int)
for fruit in fruits:
    counts_defaultdict[fruit] += 1
print(f'defaultdict 사용 결과: {dict(counts_defaultdict)}')


# collections.counter
from collections import Counter

fruits_counter = Counter(fruits)
print(f'Counter 사용 결과 : {dict(fruits_counter)}')

top1_fruits = fruits_counter.most_common(1)
print(f'가장 많이 등장한 과일 1위: {top1_fruits}')