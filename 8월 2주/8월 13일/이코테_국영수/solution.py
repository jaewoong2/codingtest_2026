from re import I
import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


# 국어 [0 for _ in range (1, 100)]
# 양어 [0 for _ in range (1, 100)]
# 수학 [0 for _ in range (1, 100)]
# 이름 set()


def compare(s1, s2):
    s1_name, s1_korean, s1_english, s1_math = s1
    s2_name, s2_korean, s2_english, s2_math = s2

    if s1_korean > s2_korean:
        return True

    if s1_korean < s2_korean:
        return False

    if s1_english < s2_english:
        return True

    if s1_english > s2_english:
        return False

    if s1_math > s2_math:
        return True

    if s1_math < s2_math:
        return False

    return s1_name < s2_name


def quick_sort(arrs):
    if len(arrs) <= 1:
        return arrs

    pivot = arrs[0]
    left_arr = [x for x in arrs[1:] if compare(x, pivot)]
    right_arr = [x for x in arrs[1:] if compare(pivot, x)]

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


def solution():
    n = int(input())
    studentes = []
    for _ in range(n):
        name, korean, english, math = input().split()
        studentes.append([name, int(korean), int(english), int(math)])

    studentes = quick_sort(studentes)

    return [x[0] for x in studentes]


if __name__ == "__main__":
    result = solution()
    print(result)
