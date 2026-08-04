import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# 문제
# N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 떄 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 * 5 얼음틀 예시에서는 아이스크림이 총 3개 생성된다.
# 입력
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)
# 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
# 출력
# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.


## 주의 해야 할 점은
def solution():
    N, M = map(int, input().split())
    maps = [[int(x) for x in input() if x != "\n"] for _ in range(N)]
    visited = set()
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(row, col):
        import collections

        queue = collections.deque()

        queue.append((row, col))

        while len(queue) > 0:
            r, c = queue.popleft()

            for i in range(4):
                dr, dc = moves[i]
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if maps[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

    result = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                continue

            if (i, j) not in visited:
                visited.add((i, j))
                bfs(i, j)
                result += 1

    return result


if __name__ == "__main__":
    result = solution()
    print(result)
