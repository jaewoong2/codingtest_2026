import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# 1 3 1 5 6 7 8 9
# 만약 0번을 털면 1번을 못텀 -> 2번 or 3번을 털어야함
# -> 2번을 털면 4번 or 5번을 털어야함 / 3번을 털면 5번
# 만약 1번을 털면 2번을 못텀 -> 3번 or 4번을 털어야함


# 7번 까지 와서 최대값 경우의 수는
# max(6번을 터는 경우의수, 5번+7번)

# f(n) = max(f(n-1), f(n - 2))

# f(0) = arr[0], f(1) = arr[1]


def solution():
    n = int(input())
    arr = [x for x in map(int, input().split())]
    dp = [arr[0], max(arr[0], arr[1])]

    for i in range(2, n):
        dp.append(max(dp[i - 1], dp[i - 2] + arr[i]))

    return dp[n - 1]


if __name__ == "__main__":
    result = solution()
    print(result)
