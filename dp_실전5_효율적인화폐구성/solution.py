import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# c


def solution():
    n, target = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [float("INF") for _ in range(target + 1)]
    dp[0] = 0

    for coin in coins:
        if coin > target:
            continue
        dp[coin] = 1

    for value in range(1, target + 1):
        for coin in coins:
            if value >= coin and dp[value - coin] != float("INF"):
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[target] == float("INF") and -1 or dp[target]


if __name__ == "__main__":
    result = solution()
    print(result)
