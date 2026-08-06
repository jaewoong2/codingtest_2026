import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def solution2():
    n, m = map(int, input().split())
    arr = [x for x in map(int, input().split())]
    balls = [0 for _ in range(m + 1)]
    result = 0

    for ball in arr:
        balls[ball] += 1

    choiceable = n
    for i in range(m + 1):
        choiceable = choiceable - balls[i]
        result += balls[i] * choiceable

    return result


def solution():
    from itertools import combinations

    n, m = map(int, input().split())
    arr = [x for x in map(int, input().split())]
    balls = [0 for _ in range(m + 1)]
    result = len([x for x in combinations(range(n), 2)])
    for ball in arr:
        balls[ball] += 1

    for ball in balls[1:]:
        if ball > 1:
            result = result - len([x for x in combinations(range(ball), 2)])

    return result


if __name__ == "__main__":
    result = solution2()
    print(result)
