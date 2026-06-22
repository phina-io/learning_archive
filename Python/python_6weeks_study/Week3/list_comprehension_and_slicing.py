# 리스트 List

# 리스트 컴프리헨션과 데이터 필터링 (List Comprehension)
numbers = [1, 2, 3, 4, 5, 6]


# for 활용한 숫자의 제곱 리스트 만들기
squares_loop = []
for num in numbers:
    squares_loop.append(num * num)
print(f'for 루프 사용: {squares_loop}')


# 리스트 컴프리헨션 사용
# [표현식 for 항목 in 반복가능객체]
squares_comp = [num * num for num in numbers]
print(f'컴프리헨션 사용: {squares_comp}')


# for 활용한 짝수 리스트 만들기
evens_loop = []
for num in numbers:
    if num % 2 == 0:
        evens_loop.append(num)
print(f'for 루프와 if문 사용: {evens_loop}')


# 리스트 컴프리헨션 사용
# [표현식 for 항목 in  반복가능객체 if 조건문]
evens_comp = [num for num in numbers if num % 2 == 0]
print(f'컴프리헨션과 if문 사용: {evens_comp}')


# 짝수만 10배로 치환하기
processed_counts = [num * 10 if num % 2 == 0 else num for num in numbers]
print(f'짝수만 10배 치환 결과: {processed_counts}')


# 행렬 1차원 리스트로 변환
matrix = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]

flat_list = [element for row in matrix for element in row]
print(f'1차원으로 펼친 행렬: {flat_list}')


#-----------------------------------------------------------------------------
# 리스트 슬라이싱(Slicing)을 활용한 데이터 처리

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]

# 인덱스 2부터 5전까지
sub_list = numbers[2:5]
print(f'numbers[2:5]: {sub_list}')


# 처음부터 인덱스 3전까지
first_three = numbers[:3]
print(f'numbers[:3]: {first_three}')


# 인덱스 6부터 끝까지
from_six = numbers[6:]
print(f'numbers[6:]: {from_six}')


# 처음부터 끝까지 2칸 간격으로(짝수)
evens = numbers[::2]
print(f'numbers[::2]: {evens}')


# 인덱스 1부터 끝까지 2칸 간격으로(홀수)
odds = numbers[1::2]
print(f'numbers[1::2]: {odds}')


# setp을 -1로 주면 역순으로 순회
reversed_list = numbers[::-1]
print(f'numbers[::-1]: {reversed_list}')


# 인덱스 2, 3, 4의 값을 새로운 리스트로 대체
print(f'값 변경 전 {numbers}')

numbers[2:5] = [99, 98, 97]
print(f'값 변경 후 : {numbers}')


# 슬라이싱으로 가변 길이 데이터 사입 및 삭제
items = ['a', 'b', 'c', 'd', 'e']


# 기존 구간 데이터 2개, 추가 구간 데이터 4개
items[1:3] = ['X', 'Y', 'Z', 'W']    
print(f'가변 데이터 사입 후: {items}')


items[1:5]= []
print(f'슬라이싱 구간 삭제 후: {items}')