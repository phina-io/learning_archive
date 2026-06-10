# 파이썬 기초 문법 - 개념자료 


# 1. 변수와 정의와 동적 타이핑(Variables and Dynamic Typing)
# 1.1 변수의 개념적 이해
# 프로그래밍에서 변수란 메모리 상에 존재하는 특정 객체(Object)에 붙여진 이름표
# 파이썬은 변수가 객체의 주소를 가리키는 참조(Reference)방식


# 1.2 동적 타이핑 (Dynamic Typing)의 메커니즘
# 동적 타이핑이란 변수에 값이 할당되는 시점에 해당 데이터 타입을 결정

# 변수 할당과 참조의 변화
from sqlite3 import converters


data = 100
print(f'초기 타입:{type(data)}')

data = 'Algorithm'
print(f'변경 후 타입:{type(data)}')

# 참조에 의한 객체 공유
list_a = [10, 20, 30]
list_b = list_a

list_b.append(40)
print(f'list_a의 상태: {list_a}')


# 1.3 용어 해설
# 객체(Object): 파이썬에서 모든 데이터는 객체로 취급. 각 객체는 고유한 ID, 타입, 값을 가짐 
# 참조(Reference): 변수가 객체의 메모리 주소를 가리키고 있는 상태


# 2. 데이터 형 변환과 예외 처리 (Type Casting)
# 2.1 명시적 형 변환의 필수성
raw_input = "25"
age = int(raw_input)
next_year_age = age + 1
print(f'내년 예상 나이는 {next_year_age}세 입니다.')

pi = 3.14159
integer_pi = int(pi)
print(f'정수 변환 결과: {integer_pi}')


# 2.2 형 변환 시 발생할 수 있는 오류 (ValueError)
user_data = '2026년'

try:
    converted_data = int(user_data)
    
except ValueError:
    print('수치형 데이터로 변환할 수 없는 형식입니다. 전처리가 필요합니다.') 
    
    
#---------------------------------------------------------------------------
'''
동적 타이핑은 파이썬의 특징으로 변수에 값이 할당 될 때 자동으로 결정
형 변환은 필요한 연산이나 처리를 위해 데이터의 타입을 사람이 직접 변환하는 것
'''
#---------------------------------------------------------------------------
name = 'Python'
age = 35

print(f'이름의 타입은 {type(name)}, 나이의 타입은 {type(age)}')
print(f'이름: {name}, 나이: {age}세')

age_input = "35"
age_int = int(age_input)
next_year_age = age_int + 1
print(f'{name}의 27년도 나이는 {next_year_age}입니다')