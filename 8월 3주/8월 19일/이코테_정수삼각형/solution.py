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


def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        m = input()

        if len(m) > 1:
            arr.append([x for x in map(int, m.split())])
        else:
            arr.append(int(m))

    for i in range(1, n):
        m = len(arr[i])
        for j in range(m):
            temp = 0

            if j == 0:
                temp = arr[i - 1][j]

            elif j == m - 1:
                temp = arr[i - 1][j - 1]

            else:
                temp = max(arr[i - 1][j], arr[i - 1][j - 1])

            arr[i][j] += temp

    return max(arr[-1])


if __name__ == "__main__":
    result = solution()
    print(result)
