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


# 특정한 값의 전투력을 보유
# 병사를 배치 할 때 전투력이 높은 병사가 앞쪽으로 오도록 내림차순으로 배치를 하고자 함
# 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외 시키는 방법을 이용

# 남아 있는 병사의 수를 최대로 하고 싶음


# n <= 2000
# 조합은 터지겠지? (2000 * 1999 * 1998 ...)
def solution():
    n = int(input())
    soliders = [x for x in map(int, input().split())][::-1]
    dp = [1 for _ in range(n)]

    # dp[i] = soliders[i] 를 포함할때 최대 길이

    for i in range(1, n):
        for j in range(0, i):
            if soliders[i] < soliders[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return n - max(dp)


if __name__ == "__main__":
    result = solution()
    print(result)
