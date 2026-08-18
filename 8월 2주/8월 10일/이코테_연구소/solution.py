import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# 바이러스 확산을 위해서 연구소에 벽을 세워야함
# 연구소의 크기는 N M
# 연구소는 빈칸0/벽1/바이러스2
# 바이러스는 4방향으로 퍼져나갈 수 있음
# 벽을 3개를 세워야함
# 벽을 3개 세운 뒤 바이러스가 퍼질 수 없는 곳을 안전영역이라고 할때
# 안정역역의 최대 크기를 구하시오


def combination(array, target):
    result = []

    def c(start, selected):
        if len(selected) == target:
            result.append(selected[:])
            return

        for index in range(start, len(array)):
            selected.append(array[index])
            c(index + 1, selected)
            selected.pop()

    c(0, [])
    return result


def find_build_wall(candidates):
    candidates = combination(candidates, 3)

    return candidates


def destory_wall(walls, maps):
    for i, j in walls:
        maps[i][j] = 0


def move_virus(row, col, maps):
    n, m = len(maps), len(maps[0])
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            # 벗어나면 Pass
            continue

        if maps[nr][nc] == 0:
            # 빈공간이면 0
            maps[nr][nc] = 2
            move_virus(nr, nc, maps)

    return


def calculate_area(maps):
    count = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0:
                count += 1

    return count


def solution():
    n, m = map(int, input().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]

    empties = []
    viruses = []

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            maps[i][j] = row[j]

            if maps[i][j] == 0:
                empties.append([i, j])
            if maps[i][j] == 2:
                viruses.append([i, j])

    ans = -1

    for candidate in find_build_wall(empties):
        current_maps = [[col for col in row] for row in maps]

        # 3개의 벽을 지음
        for i, j in candidate:
            current_maps[i][j] = 1
        # 바이러스가 이동함
        for i, j in viruses:
            move_virus(i, j, current_maps)

        ans = max(ans, calculate_area(current_maps))

    return ans


if __name__ == "__main__":
    result = solution()
    print(result)
