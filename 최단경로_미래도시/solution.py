import dis
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

    return distances


def solution():
    n, m = map(int, input().split())
    start_node = 1
    graphs = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        a, b = map(int, input().split())

        graphs[a].append((b, 1))
        graphs[b].append((a, 1))

    x, k = map(int, input().split())

    distances_s = dijkstra(n, graphs, start_node)
    distances_k = dijkstra(n, graphs, k)

    return distances_s[k] + distances_k[x]


if __name__ == "__main__":
    result = solution()
    print(result)
