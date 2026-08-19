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
    T = int(input())
    answers = []

    for _ in range(T):
        n, m = map(int, input().split())
        maps = [[0 for _ in range(m)] for _ in range(n)]
        numbers = [x for x in map(int, input().split())]
        dp = [[0 for _ in range(m)] for _ in range(n)]
        answer = 0
        start = 0
        for i in range(n):
            maps[i] = numbers[start : start + m]
            start = start + m
            dp[i][0] = maps[i][0]

        for col in range(1, m):
            for row in range(n):
                maximum = dp[row][col - 1]

                if 0 <= row - 1:
                    maximum = max(maximum, dp[row - 1][col - 1])

                if row + 1 < n:
                    maximum = max(maximum, dp[row + 1][col - 1])

                dp[row][col] = maximum + maps[row][col]

        for row in range(n):
            answer = max(answer, dp[row][-1])

        answers.append(answer)

    return answers


if __name__ == "__main__":
    result = solution()
    print(result)
