from math import comb
import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


# 그냥 일직선 계산


# 이거 일직선 계산 쉽게하는 방법이 뭐가 있으려나...
def is_find(maps, row, col, direction):
    i, j = 1, 1
    n_row, n_col = row + i * direction[0], col + j * direction[1]

    while True:
        if not (0 <= n_row < len(maps) and 0 <= n_col < len(maps[0])):
            return False

        if maps[n_row][n_col] == "O":
            return False

        if maps[n_row][n_col] == "S":
            return True

        n_row = n_row + i * direction[0]
        n_col = n_col + j * direction[1]


def combination(arr, r):
    selected = []

    def c(start, chosen=[]):
        if len(chosen) == r:
            selected.append(chosen)
            return

        for i in range(start, len(arr)):
            c(i + 1, chosen + [arr[i]])

    c(0, [])

    return selected


def solution():
    n = int(input())
    maps = [[x for x in input().split()] for _ in range(n)]
    empties = []
    teachers = []

    for i in range(n):
        for j in range(n):
            if maps[i][j] == "T":
                teachers.append([i, j])
                continue

            if maps[i][j] == "S":
                continue

            empties.append([i, j])

    candidates = combination(empties, 3)
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for candidate in candidates:
        숨을수있습니다 = True

        for i, j in candidate:
            maps[i][j] = "O"

        for teacher_i, teacher_j in teachers:
            for dr, dc in moves:
                찾았습니다 = is_find(maps, teacher_i, teacher_j, [dr, dc])

                # 찾으면
                if 찾았습니다:
                    # 찾을 수 있습니다.
                    숨을수있습니다 = False

        if 숨을수있습니다:
            # 한번이라도 다 숨을 수 있으면 YES
            return "YES"

        for i, j in candidate:
            maps[i][j] = "X"

    return "NO"


if __name__ == "__main__":
    result = solution()
    print(result)
