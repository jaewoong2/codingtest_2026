import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

## 그리디
## -> 가장 저렴한 신장트리를 만들어라
## -> 사"이클이 없으며 모든 노드가 연결되어 있는 구조"를 말함
## -> 정렬 간선의 거리를 기준으로 오름 차순으로
## -> 사이클 판별 (서로소)


def union_find(n=0):
    parents = [int(1e19) for _ in range(n + 1)]

    for i in range(1, n + 1):
        parents[i] = i

    def find(node):
        if node != parents[node]:
            parents[node] = find(parents[node])

        return parents[node]

    def union(a, b):
        parents_a = find(a)
        parents_b = find(b)

        if parents_a > parents_b:
            parents[parents_a] = parents_a
        else:
            parents[parents_b] = parents_b

    def get():
        return parents

    return find, union, get


def solution():
    v, e = map(int, input().split())
    find, union, get_parents = union_find(v)
    graphs = {i: [] for i in range(1, v + 1)}
    edges = []

    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges = sorted(edges, key=lambda x: x[0])
    result = 0
    for w, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            result += w

    return result


if __name__ == "__main__":
    result = solution()
    print(result)
