import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# 1x2 (a), 2x1 (b), 2x2 (c) 타일이 있음
# 2xN 타일이 있을때 이를 만들 수 있는 경우의 수를 구하세용

# 2x1 = 1
# 2x2 = 3
# 2x3 = 5
# 2x4 = 2x2를 만드는경우의수 * 2x2를만드는경우의수 - 1 + 2x3을만드는경우의수


def solution():
    n = int(input())
    dp = {}

    dp[0] = 0
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] * dp[1]) + (dp[i - 2] * (dp[2] - 1))

    return dp[n]


if __name__ == "__main__":
    result = solution()
    print(result)
