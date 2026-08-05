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


def solution():
    from collections import deque

    v, e = map(int, input().split())
    indegrees = [0 for _ in range(v + 1)]
    graphs = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        indegrees[b] += 1
        graphs[a].append(b)

    queue = deque([])
    response = []

    for i in range(1, v + 1):
        if indegrees[i] == 0:
            queue.append(i)

    while len(queue) > 0:
        node = queue.popleft()
        response.append(node)

        for next_node in graphs[node]:
            indegrees[next_node] -= 1

            if indegrees[next_node] == 0:
                queue.append(next_node)

    return response


if __name__ == "__main__":
    result = solution()
    print(result)
