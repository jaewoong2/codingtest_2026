import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# X가 5로 나눠질때 5로 나눈다
# X가 3로 나눠질때 3로 나눈다
# X가 2로 나눠질때 2로 나눈다
# X를 1로 뺀다

# X가 1이 되게 하는 최소 "방법의 가지수"

# X = 1) 0
# X = 2) 1
# X = 3) 1
# X = 4) 2
# X = 5) 1
# X = 6) 1 + (X=3) or (X=5)
# X = 7) 1 + (X=6)
# X = 8) 1 + (X=4) or 1 + (X=7)

# result = 1 + f(x-1) -> 최대경우의수
# X>1 / X = 2로 나눠지는 경우) result = min(result, 1+f(x//2))
# X>1 / X = 3로 나눠지는 경우) result = min(result, 1+f(x//3))
# X>1 / X = 5로 나눠지는 경우) result = min(result, 1+f(x//5))


def solution():
    X = int(input())

    results = {0: 0, 1: 1, 2: 1, 3: 1, 5: 1}

    for i in range(2, X + 1):
        if i in results:
            continue
        result = results[i - 1] + 1

        if i % 2 == 0:
            result = min(result, results[i // 2] + 1)

        if i % 3 == 0:
            result = min(result, results[i // 3] + 1)

        if i % 5 == 0:
            result = min(result, results[i // 5] + 1)

        results[i] = result
    return results[X]


if __name__ == "__main__":
    result = solution()
    print(result)
