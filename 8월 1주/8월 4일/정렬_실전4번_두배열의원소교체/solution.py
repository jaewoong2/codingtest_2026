import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    left = 1
    right = len(array) - 1

    while left <= right:

        while left <= right and pivot >= array[left]:
            left += 1

        while left <= right and pivot <= array[right]:
            right -= 1

        if left > right:
            break

        array[left], array[right] = array[right], array[left]

    return quick_sort(array[1:left]) + [pivot] + quick_sort(array[right + 1 :])


def solution():
    n, k = map(int, input().split())
    arr_a = quick_sort([x for x in map(int, input().split())])
    arr_b = quick_sort([x for x in map(int, input().split())])

    for i in range(k):
        if arr_a[i] >= arr_b[(n - 1) - i]:
            break

        arr_a[i], arr_b[(n - 1) - i] = arr_b[(n - 1) - i], arr_a[i]

    return sum(arr_a)


if __name__ == "__main__":
    result = solution()
    print(result)
