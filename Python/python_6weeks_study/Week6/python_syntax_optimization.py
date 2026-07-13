# 1. 리스트 컴프리헨션(List Comprehension): 데이터 정제와 변환
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 일반적인 for문
traditional_way = []
for n in numbers:
    if n % 2 == 0:
        traditional_way.append(n ** 2)
        
# 리스트 컴프리헨션 
# [(표현식) for (항목) in (반복가능객체) if (조건식)]
optimized_way = [n ** 2 for n in numbers if n % 2 == 0]

print(f"전통적 방식: {traditional_way}")
print(f"최적화 방식: {optimized_way}")


# -------------------------------------------------------------
# 2. 데이터 바인딩(Data Binding): Zip과 언패킹(Unpacking)
names = ["철수", "영희", "민수"]
scores = [90, 85, 70]

# zip을 활용한 병렬 순회
for name, score in zip(names, scores):
    print(f"학생: {name}, 점수: {score}")
    
# 딕셔너리로의 즉시 변환 
student_db = dict(zip(names, scores))

print(f"생성된 DB: {student_db}")
print(f"민수의 점수: {student_db.get('민수')}")


# -------------------------------------------------------------
# 3. 집합(Set): 해시 기반의 초고속 연산
listA = [1, 5, 2, 3, 1, 2]
listB = [2, 3, 4, 5, 9]

# 비효율적 방식
bad_result = []
for x in listA:
    if x in listB and x not in bad_result:
        bad_result.append(x)
        
# 집합 연산 방식
setA = set(listA)
setB = set(listB)

# 교집합 연산
common = setA & setB

#결과정렬
result = sorted(list(common))

print(f"집합 기반 결과: {result}")


# -------------------------------------------------------------
# 4. 빈도수 계산 최적화: Dictionary와 Counter
from collections import Counter, defaultdict

s = "mississippi"

# defaultdict를 이용한 수동 카운팅
counts = defaultdict(int)
for char in s:
    counts[char] += 1
    
#  Counter를 이용한 전문가형 구현
freq = Counter(s)
print(freq)