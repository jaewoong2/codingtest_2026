import sys
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    result = 0

    while n != 1:
        while n % k > 0:
            n = n - 1
            result += 1

        while n % k == 0:
            n = n // k
            result += 1

    return result


if __name__ == "__main__":
    result = solution()
    print(result)
