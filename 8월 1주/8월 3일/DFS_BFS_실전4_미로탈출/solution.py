import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


## 주의 해야 할 점은
def solution():
    N, M = map(int, input().split())
    maps = [[int(x) for x in input().rstrip()] for _ in range(N)]
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def bfs(r, c):
        from collections import deque

        queue = deque()
        queue.append((r, c))

        while len(queue) > 0:
            row, col = queue.popleft()

            if row == N - 1 and col == M - 1:
                return maps[row][col]

            for dr, dc in moves:
                nr, nc = row + dr, col + dc

                if 0 <= nr < N and 0 <= nc < M:
                    if maps[nr][nc] == 1:
                        queue.append((nr, nc))
                        maps[nr][nc] = maps[row][col] + 1

    return bfs(0, 0)


if __name__ == "__main__":
    result = solution()
    print(result)
