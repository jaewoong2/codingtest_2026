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
    n, k = map(int, input().split())
    maps = [[0 for _ in range(n)] for _ in range(n)]
    viruses = [[] for _ in range(k + 1)]

    for i in range(n):
        row = [x for x in list(map(int, input().split()))]
        for j in range(n):
            maps[i][j] = row[j]

            if maps[i][j] > 0:
                viruses[maps[i][j]].append([i, j])

    s, r, c = map(int, input().split())

    # 바이러스를 순서대로 퍼트림 -> bfs
    def bfs():
        import collections

        queue = collections.deque()
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for virus in viruses[1:]:
            for row, col in virus:
                queue.append([row, col, 0])

        while queue:
            cr, cc, time = queue.popleft()

            for dr, dc in moves:
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < n and 0 <= nc < n:
                    if maps[nr][nc] == 0 and time + 1 <= s:
                        maps[nr][nc] = maps[cr][cc]
                        queue.append((nr, nc, time + 1))

    bfs()

    return maps[r - 1][c - 1]


if __name__ == "__main__":
    result = solution()
    print(result)
