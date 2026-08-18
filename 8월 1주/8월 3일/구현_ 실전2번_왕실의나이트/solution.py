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
# 8 x 8 좌표 평면
# 나이트는
# 수평 으로 두 칸 이동 한 뒤에 수직으로 한 칸 이동하기
# 수직 으로 두 칸 이동 한 뒤에 수평으로 한 칸 이동하기

# 나이트의 위치가 주어 졌을 때 나이트가 이동 할 수 있는 경우의 수를 출력

# 최대 8가지 경우의 수


def solution():
    row, col = [x for x in input()]
    a = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    row, col = a[row], int(col) - 1

    moves = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

    result = 0

    for drow, dcol in moves:
        n_row, n_col = row + drow, col + dcol

        if n_row >= 0 and n_col >= 0 and n_row <= 7 and n_col <= 7:
            result += 1

    return result


if __name__ == "__main__":
    result = solution()
    print(result)
