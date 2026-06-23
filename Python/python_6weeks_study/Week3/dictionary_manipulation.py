# 딕셔러니 Dict
# 이름과 점수 리스트를 딕셔너리로 매핑
names = ['하늘', '하나', '바다']
score = [90, 85, 70]

student_info = dict(zip(names, score))
print(f'매핑된 딕셔너리: {student_info}')
print(f'하늘의 점수: {student_info["하늘"]}')


# 딕셔너리 컴프리헨션
student_info = {'하늘': 90, '하나': 85, '바다': 70}

excellent_student = {
    name: score + 5 
    for name, score in student_info.items() 
    if score >= 80
}
print(f'우수 학생 가산점 결과: {excellent_student}')


# get()메서드와 삼항 연산자
students = {'하늘': 90, '하나': 85}

data_1 = students.get('태양', '미응시')
data_2 = students['태양'] if '태양' in students else '미응시'

print(f'태양 점수(get): {data_1}')
print(f'태양 점수(삼항): {data_2}')


# 데이터 일괄 수정 및 병합
student_data = {'하늘': 90, '하나': 85, '바다': 70}
new_data = {'태양': 75, '바다': 80}
student_data.update(new_data)

print(f'업데이트된 정보: {student_data}')


# 딕셔너리 반복
for name in student_data.keys():
    print(f'이름: {name}')
    
for score in student_data.values():
    print(f'점수: {score}')
    
for name, score in student_data.items():
    print(f'{name}의 점수: {score}')
    
    
# 2차원 중첩 딕셔너리
company_branches = {
    '서울 본사': {
        '매니저': '하늘',
        '직원수': 13,
        '프로젝트': ['AI_Chatbot', 'Data_Clund']
    },
    '부산 지사': {
        '매니저' : '하나',
        '직원수': 5,
        '프로젝트': ['Logistics_System']
    }
}

seoul_projects = company_branches['서울 본사']['프로젝트']
print(f'서울 본사 진행 프로젝트: {seoul_projects}')


# collections.defaultdict
from collections import defaultdict
raw_data = [
    ('개발팀', '하늘'), 
    ('개발팀', '하나'), 
    ('인사팀', '바다'), 
    ('마케팅팀', '태양')
]

department_json = defaultdict(list)

for dept, name in raw_data:
    department_json[dept].append(name)
    
print(f'부서별 직원 명단: {dict(department_json)}')


# JSON 데이터 변환
import json

staff_info = {
    'name': '하늘',
    'age': 30,
    'addr': '서울'
}

json_string = json.dumps(staff_info, ensure_ascii=False)
print(f'변환된 JSON 문자열: {json_string}')
print(f'타입 확인: {type(json_string)}')

received_dict = json.loads(json_string)
print(f'다시 파이썬 딕셔너리로: {received_dict["name"]}')