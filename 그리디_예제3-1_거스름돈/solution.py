import sys
import os
if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

def solution():
    price = int(input())
    coins = [500, 100, 50, 10]
    result = 0
    for coin in coins:
        result += price // coin
        price = price % coin

    return result


if __name__ == "__main__":
    response = solution()
    print(response)
