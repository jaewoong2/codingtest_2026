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
    times = []
    values = []
    dp = [0 for _ in range(n + 1)]

    for _ in range(n):
        time, value = map(int, input().split())

        times.append(time)
        values.append(value)

    # dp[n] = n일 이후로 퇴사 날까지 최대로 벌 수 있는 돈
    # dp[n] = dp[n] = value[n] + dp[n + times[n]]

    for i in range(n - 1, -1, -1):
        time = i + times[i]
        if time <= n:
            dp[i] = max(values[i] + dp[time], dp[i + 1])
        else:
            dp[i] = dp[i + 1]

    return max(dp)


if __name__ == "__main__":
    result = solution()
    print(result)
