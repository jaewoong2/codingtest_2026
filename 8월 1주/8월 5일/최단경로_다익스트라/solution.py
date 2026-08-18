import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def dijkstra(n, graphs, start):
    import heapq

    distances = [int(1e9) for _ in range(n + 1)]
    distances[start] = 0
    queue = []

    heapq.heappush(queue, (0, start))

    while len(queue) > 0:
        value, node = heapq.heappop(queue)

        if distances[node] < value:
            continue

        for next_node, weight in graphs[node]:

            if distances[next_node] <= weight + value:
                continue

            distances[next_node] = weight + value
            heapq.heappush(queue, (distances[next_node], next_node))

    return distances[1:]


def solution():
    n, m = map(int, input().split())
    start_node = int(input())
    graphs = {}

    for _ in range(m):
        a, b, c = map(int, input().split())

        if a not in graphs:
            graphs[a] = []

        if b not in graphs:
            graphs[b] = []

        graphs[a].append((b, c))
        graphs[b].append((a, c))

    return dijkstra(n, graphs, start_node)


if __name__ == "__main__":
    result = solution()
    print(result)
