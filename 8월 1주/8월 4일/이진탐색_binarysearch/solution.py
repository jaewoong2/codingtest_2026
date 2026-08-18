import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def binary_search(array, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] > target:
        return binary_search(array, start, mid - 1, target)

    if array[mid] < target:
        return binary_search(array, mid + 1, end, target)

    if array[mid] == target:
        return mid + 1


def binanry_search_loop(array, target):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1

        elif array[mid] > target:
            end = mid - 1

        else:
            return mid + 1

    return None


def solution():
    n, target = map(int, input().split())
    array = [x for x in map(int, input().split())]

    return binary_search(array, 0, n - 1, target)


if __name__ == "__main__":
    result = solution()
    print(result)
