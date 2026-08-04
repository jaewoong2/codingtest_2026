import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

############
# while left_index <= right_index and arr[left_index] <= pivot:
#     left_index += 1

# while left_index <= right_index and arr[right_index] >= pivot:
#     right_index -= 1

# left  → 피벗보다 큰 값을 찾으러 오른쪽으로 이동
# right → 피벗보다 작은 값을 찾으러 왼쪽으로 이동
# left > right → 더 이상 swap하지 않고 종료
############


def quick_sort(arr=[]):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    length = len(arr)

    left_index = 1
    right_index = length - 1

    while left_index <= right_index:

        while left_index <= right_index and arr[left_index] <= pivot:
            left_index += 1

        while left_index <= right_index and arr[right_index] >= pivot:
            right_index -= 1

        if left_index > right_index:
            break

        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]

    return quick_sort(arr[1:left_index]) + [pivot] + quick_sort(arr[1 + right_index :])


def solution():
    arr = [x for x in map(int, input().split())]

    print(arr)

    return quick_sort(arr)


if __name__ == "__main__":
    result = solution()
    print(result)
