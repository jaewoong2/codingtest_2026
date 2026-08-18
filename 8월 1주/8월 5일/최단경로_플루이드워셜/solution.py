import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def fluid(n, graphs):
    distances = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        distances[i][i] = 0

        for node, distance in graphs[i]:
            distances[i][node] = distance

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )

    return distances


def solution():
    n, m = map(int, input().split())
    graphs = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graphs[a].append((b, c))

    result = fluid(n, graphs)

    for i in range(1, n + 1):
        print(result[i][1:])


if __name__ == "__main__":
    result = solution()
    print(result)
