from re import I
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
    n = int(input())
    cards = []

    for _ in range(n):
        card = int(input())
        cards.append(card)

    cards = sorted(cards, reverse=True)
    total = 0

    while len(cards) > 1:
        a, b = cards.pop(), cards.pop()
        cards.append(a + b)
        total += a + b
        cards = sorted(cards, reverse=True)

    return total


if __name__ == "__main__":
    result = solution()
    print(result)
