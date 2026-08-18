import sys
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def solution():
    n, m, k = map(int, input().split())
    arr = sorted([x for x in map(int, input().split())], reverse=True)

    a, b = arr[0], arr[1]
    result = 0

    result += (a * k + b) * m // (k + 1)
    result += a * (m % (k + 1))

    return result


if __name__ == "__main__":
    result = solution()
    print(result)
