import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def tree(node):
    nodes = {
        "left": [],
        "right": [],
    }

    def add(value):
        # 작은 값은 왼쪽
        if value < node:
            if nodes["left"] == []:
                nodes["left"] = tree(value)
            else:
                # 왼쪽 자식에게 삽입을 맡김
                nodes["left"][0](value)

        # 큰 값은 오른쪽
        elif value > node:
            if nodes["right"] == []:
                nodes["right"] = tree(value)
            else:
                # 오른쪽 자식에게 삽입을 맡김
                nodes["right"][0](value)

        # 같은 값은 무시
        else:
            pass

    def get_left_node():
        return nodes["left"]

    def get_right_node():
        return nodes["right"]

    def get_value():
        return node

    return [add, get_left_node, get_right_node, get_value]


def solution():
    n, target = map(int, input().split())
    nodes = [x for x in map(int, input().split())]

    root = tree(nodes[0])

    for value in nodes[1:]:
        root[0](value)

    print_tree(root)


def print_tree(node, depth=0, direction="root"):
    if node is None:
        return
    if node == []:
        return
    left_node, right_node = node[1](), node[2]()
    # 오른쪽을 위에 출력
    print_tree(right_node, depth + 1, "R")

    print("    " * depth + f"{direction}: {node[3]()}")

    # 왼쪽을 아래에 출력
    print_tree(left_node, depth + 1, "L")


if __name__ == "__main__":
    result = solution()
    print(result)
