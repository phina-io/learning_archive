# [병렬 처리와 인덱스] 효율적인 루프 구성
# Zip을 활용한 데이터 매핑
list_1 = [1, 2, 3, 4]
list_2 = ['2000원', '1500원', '700원', '2500원']
list_3 = ['사과', '딸기', '바나나', '체리']

zipped_1 = zip(list_1, list_2)
zipped_2 = zip(list_1, list_3, list_2)
print(list(zipped_1))
print(list(zipped_2))

for num, letter in zip(list_1, list_3):
    print(f'{num} is paired with "{letter}"')

list_4 = ['부사', '설향']
for variety, name in zip(list_4, list_3):
    print(f'종류: {variety}, 과일명: {name}') # 짝이 없는 품목은 출력되지 않음


# Enumerate를 활용한 조건부 인덱스 찾기
for index, value in enumerate(list_3, 1):
    print(f'{index}번 과일: {value}')

for index, value in enumerate(list_3, 1):
    if value == '바나나':
        print(f'바나나는 {index}번에 있습니다.')
        break

for index, price in enumerate(list_2, 1):
    if index % 2 == 0:
        print(f'{index}번째 가격: {price}')