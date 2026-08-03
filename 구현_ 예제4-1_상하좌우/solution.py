import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


# 구현 해야 할 때 신경 써야 하는 것
# 1. 맵 밖으로 나가는것 을 막아야함
# 2. 그리고 0, 0 이 아니라 1, 1 시작이라는 것을 알아야함
# 3. R -> (1, 0), U -> (0,- 1), D (0, 1), L (-1, 0)
# 4. n x n 맵


def solution():
    n = int(input())
    plans = map(str, input().split())
    moves = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    row, col = 0, 0

    for plan in plans:
        d_row, d_col = moves[plan]

        n_row, n_col = row + d_row, col + d_col

        if n_row >= n or n_col >= n:
            continue

        if n_row < 0 or n_col < 0:
            continue

        row, col = n_row, n_col

    return [row + 1, col + 1]


if __name__ == "__main__":
    result = solution()
    print(result)
