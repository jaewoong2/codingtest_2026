import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


# x 에서 최단거리가 k인 도시의 번호를 한줄에 하나씩 오름차순으로 출력
# 다익스트라? BFS?
def solution():
    n, m, k, x = map(int, input().split())
    graphs = {i + 1: [] for i in range(n)}

    for _ in range(m):
        a, b = map(int, input().split())
        graphs[a].append(b)

    def dijkstra(start):
        import heapq

        q = []
        heapq.heappush(q, (0, start))

        distances = [int(1e20) for _ in range(n + 1)]
        distances[start] = 0

        while q:
            distance, node = heapq.heappop(q)

            if distance > distances[node]:
                continue

            for next_node in graphs[node]:
                if distances[next_node] > distance + 1:
                    distances[next_node] = distance + 1
                    heapq.heappush(q, (distance + 1, next_node))

        return distances

    def bfs(start):
        import collections

        queue = collections.deque()
        queue.append((start, 0))
        distances = [int(1e10) for _ in range(n + 1)]
        distances[start] = 0

        while queue:
            node, distance = queue.popleft()

            for next_node in graphs[node]:
                if distances[next_node] > distance + 1:
                    distances[next_node] = distance + 1
                    queue.append((next_node, distance + 1))

        return distances

    distances = dijkstra(x)

    for i in range(len(distances)):
        if distances[i] == k:
            print(i)
    else:
        print(-1)
    return distances


if __name__ == "__main__":
    result = solution()
    print(result)
