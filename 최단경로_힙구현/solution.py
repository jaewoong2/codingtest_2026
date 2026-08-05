import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def heap():
    queue = []

    def heappush(node):
        child_index = len(queue)
        queue.append(node)

        while child_index > 0:
            parent_index = (child_index - 1) // 2

            if queue[parent_index][0] <= queue[child_index][0]:
                break

            queue[parent_index], queue[child_index] = (
                queue[child_index],
                queue[parent_index],
            )
            child_index = parent_index

    def heappop():
        if len(queue) == 0:
            return -1

        if len(queue) == 1:
            return queue.pop()

        if len(queue) == 2:
            if queue[0][0] < queue[1][0]:
                queue[1], queue[0] = queue[0], queue[1]

            return queue.pop()

        smallest_node = queue[0]
        queue[0] = queue.pop()
        parent = 0

        while True:
            left = parent * 2 + 1

            if left >= len(queue):
                break

            right = left + 1
            smallest = left

            if right < len(queue) and queue[right][0] < queue[left][0]:
                smallest = right

            if queue[parent][0] <= queue[smallest][0]:
                break

            queue[parent], queue[smallest] = queue[smallest], queue[parent]
            parent = smallest

        return smallest_node

    def get_queue():
        return queue

    return [heappush, heappop, get_queue]


def dijkstra(n, graphs, start):
    heappush, heappop, get_queue = heap()

    distances = [int(1e9) for _ in range(n + 1)]
    distances[start] = 0

    heappush((0, start))

    while len(get_queue()) > 0:
        value, node = heappop()  # type: ignore

        if distances[node] < value:
            continue

        for next_node, weight in graphs[node]:

            if distances[next_node] <= weight + value:
                continue

            distances[next_node] = weight + value
            heappush((distances[next_node], next_node))

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
