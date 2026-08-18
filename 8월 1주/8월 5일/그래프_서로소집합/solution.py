import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def union_find(n):
    parents = [-1 for _ in range(n + 1)]

    for i in range(1, n + 1):
        parents[i] = i

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a < parent_b:
            parents[b] = parent_a
        else:
            parents[a] = parent_b

    def get_parents():
        return parents

    return find, union, get_parents


def solution():
    v, e = map(int, input().split())
    find, union, get_parents = union_find(v)

    for _ in range(e):
        a, b = map(int, input().split())
        union(a, b)

    for i in range(1, v + 1):
        find(i)

    return get_parents()[1:]


if __name__ == "__main__":
    result = solution()
    print(result)
