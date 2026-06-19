# [데이터 구조화] 언패킹과 멤버십 테스트
# 튜플 언패킹

# 기본 변수 할당
data = ('python', 20)

name, age = data
print(f'이름: {name}, 나이: {age}')


# 변수 값 교환
a = 10
b = 20
print(f'교환 전: a={a}, b={b}')

a, b = b, a #(b, a)라는 새로운 튜플을 만들어 a, b에 각각 언패킹
print(f'교환 후: a={a}, b={b}')


# for문 활용
person_data = [('Luna', 20), ('Bella', 15), ('Mia', 17)]
print('\n회원 명단')
for name, age in person_data:
    print(f'이름:{name}, 나이:{age}')
    

# * 확장 언패킹
log_entry = ('[ERROR]', '2026-06-19', 'Database', 'Connection', 'Failed')
tag, *message_parts = log_entry

print(f'로그 태그: {tag}')
print(f'메시지 내용: {message_parts}')
print(f'실제 메시지: {" ".join(message_parts)}')


# 특정 값 무시하기
person_data = ('Luna', 20, 'seoul', '010-1234-5678')
name, _, city, _ = person_data
print(f'이름: {name}, 도시: {city}')


#-------------------------------------------------------------------------------------------
# In 연산자를 활용한 존재 여부 확인
fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)
print('grape' in fruits)


# if문 사용
buy_fruit = 'grape'
if buy_fruit in fruits:
    print(f'{buy_fruit}는 있습니다. 장바구니에 추가하지 않습니다.')
else:
    print(f'{buy_fruit}는 없습니다. 장바구니에 추가 해야합니다.')


# not in 사용
new_fruit = 'grape'
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print(f'{new_fruit} 구매 완료. 현재 나의 과일: {fruits}')


# set과 활용하기
users = {'Luna20', 'bad_hacker', 'Bella15'}

bad_users = 'bad_hacker'

if bad_users in users:
    print(f'경고: {bad_users}가 존재 합니다. 확인이 필요합니다')


# 딕셔너리와 활용
attendence = {'Luna': '출석',
              'Bella': '지각',
              'Mia': '결석'}

student = 'Mia'
status = attendence[student] if student in attendence else'명단에 없음'

print(f'student 학생의 상태: {status}')