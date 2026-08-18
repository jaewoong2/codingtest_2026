import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# DFS 로 하면 스택이 쌓일 수 있기 때문에,
# 굳이 DFS로 안하고 BFS로 해당 i,j 에서 탐색 할 수 있는 모든걸 return 하는
# 식으로 진행 하는게 더 좋을 수 도 있엇으


def solution():
    n, l, r = map(int, input().split())
    maps = [[x for x in map(int, input().split())] for _ in range(n)]

    count = 0
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def dfs(row, col, visited):
        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < n and 0 <= nc < n:
                if (nr, nc) not in visited:
                    if l <= maps[row][col] - maps[nr][nc] <= r:
                        visited.add((nr, nc))
                        dfs(nr, nc, visited)

                    elif l <= maps[nr][nc] - maps[row][col] <= r:
                        visited.add((nr, nc))
                        dfs(nr, nc, visited)

    count = 0
    while True:
        all_visited = set()
        nodes = []

        for i in range(n):
            for j in range(n):
                if (i, j) not in all_visited:
                    visited = set()
                    visited.add((i, j))
                    dfs(i, j, visited)

                    for a, b in visited:
                        all_visited.add((a, b))

                    nodes.append(visited)

        is_break = True
        for values in nodes:
            if len(values) > 1:
                is_break = False
                total = sum(maps[a][b] for a, b in values)
                result = total // len(values)

                for a, b in values:
                    maps[a][b] = result

        if is_break:
            break

        count += 1

    return count


if __name__ == "__main__":
    result = solution()
    print(result)
