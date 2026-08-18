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
    string = [int(x) for x in str(input())]

    zeros = 0
    ones = 0

    last = string[0]
    for i in range(1, len(string)):
        if last != string[i]:
            if last == 0:
                zeros += 1
            else:
                ones += 1

            last = string[i]

    if last == 0:
        zeros += 1
    else:
        ones += 1

    return min(zeros, ones)


if __name__ == "__main__":
    result = solution()
    print(result)
