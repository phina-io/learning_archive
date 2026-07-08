#  해시 기반 카운팅 최적화 (collections.Counter)

# 1. 빈도 분석의 효율적 접근
# 데이터의 출현 빈도를 계산 할 때 이중 반복문을 사용하면 제곱의 시간이 소요 되지만 
# 해시 테이블 구조인 Counter를 사용하면 단 한 번의 순회로 통계 정보 추출


# 2. 최빈값 추출과 애너그램(Anagram) 판별
# 애너그램이란 문자의 순서를 바꾸어 다른 단어를 만드는 것. 두 문자열의 구성 문자와 개수가 완벽하게 일치해야 함
from collections import Counter

# 최빈값 추출
data = [1, 2, 2, 3, 3, 3]
counter = Counter(data)

most_frequent = counter.most_common(1)[0][0]
print(f"최빈값: {most_frequent}")

# 에너그램 판별
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
print(f"listen & silent 애너그램 여부: {is_anagram('listen', 'silent')}")


# 3. 두 단어의 애너그램 관계 확인
def is_angram(word1, word2):
    return Counter(word1) == Counter(word2)

word1 = "listen"
word2 = "silent"
word3 = "hello"

print(f"'{word1}'와 '{word2}'는 애너그램인가? {is_anagram(word1, word2)} ")
print(f"'{word1}'와 '{word3}'는 애너그램인가? {is_anagram(word1, word3)} ")


# 4. 흩어진 데이터 합치고 빼기
martA = Counter(["사과", "바나나", "사과", "멜론"])
martB = Counter(["사과", "바나나", "체리", "체리"])

total_stock = martA + martB
print(f"두 마트의 총 재고: {total_stock}")

difference = martA - martB
print(f"A마트에만 더 많은 나은 재고: {difference}")


# Counter 차집합
participants = ["bob", "stanko", "mislav", "ana"]
completions = ["stanko", "ana", "mislav"]

incomplete = Counter(participants) - Counter(completions)
print(f"완주하지 못한 선수 데이터: {incomplete}")

result_player = list(incomplete.keys())[0]
print(f"최종 탈락자: {result_player}")


# Counter 교집합
bagA = Counter(["루비", "루비", "사파이어", "진주"])
bagB = Counter(["루비", "진주", "루비"])

common_jewelry = bagA & bagB
print(f"공통으로 겹치는 보석과 개수: {common_jewelry}")
print(f"총 공통 보석 개수: {sum(common_jewelry.values())}")