# 커스텀 정렬과 익명 함수 (Lambda Sort)

# 1. key 매개변수와 정렬 원리
# sort()와 sorted() 함수는 key 매개변수를 통해 정렬 기준을 사용자가 정의할 수 있는 강력한 기능을 제공


# 2. 람다(Lambda)식을 활용한 다중 조건 정렬
# 특정 인덱스의 문자로 정렬하고 같으면 사전순 정렬
def custom_sort_example(strings, n):
    # strings의 각 원소 x에 대해 
    # 1순위 x[n] (n번째 글자) 기준 오름차순
    # 2순위 x (문자열 전체) 기준 사전순 오름차순
    sorted_list = sorted(strings, key=lambda x: (x[n], x))
    return sorted_list

strings = ["abce", "abcd", "cdx"]
n = 1
print(f"정렬 결과: {custom_sort_example(strings, n)}")


# lambda를 활용한 사용자 정의 정렬
students = [
    ("Alice", 90, 1996),
    ("Bob", 88, 1994),
    ("Charlie", 90, 1996)
]

# 1. 점수 기준으로 내림차순 정렬
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"점수 기준 내림차순: {sorted_by_score}")

# 2. 다중 조건 정렬
# 1순위 점수 내림차순, 2순위 출생년도 오름차순
sorted_multiple = sorted(students, key=lambda x: (-x[1], x[2]))
print(f"다중 조건 정렬: {sorted_multiple}")


# 문자열 길이 기준 정렬
# 1순위 글자 수 짧은 순 2순위 사전순
words = ["apple", "banana", "ace", "cat", "bad"]

sorted_words = sorted(words, key=lambda x: (len(x), x))
print(f"길이 및 사전순 정렬: {sorted_words}")


# 2차원 좌표 정렬
# X좌표 오름차순, Y좌표 내림차순
points = [
    (2, 3),
    (1, 2),
    (2, 5),
    (1, 8)
]

sorted_points = sorted(points, key=lambda x: (x[0], -x[1]))
print(f"좌표 다중 정렬: {sorted_points}")