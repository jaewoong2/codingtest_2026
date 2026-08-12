import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


# 연산자의 순서를 정해서 최소/최대를 구하는 문제
# DFS로 그냥 돌리면 될거 같기는 한데........ 10*10


def solution():
    n = int(input())
    numbers = [x for x in map(int, input().split())]
    commands = [x for x in map(int, input().split())]
    ans = [-1 * int(1e20), int(1e20)]

    def dfs(operators, index, total):
        if index == n:
            ans[0] = max(ans[0], total)
            ans[1] = min(ans[1], total)
            return

        if operators[0] > 0:
            operators[0] -= 1
            dfs(operators, index + 1, total + numbers[index])
            operators[0] += 1

        if operators[1] > 0:
            operators[1] -= 1
            dfs(operators, index + 1, total - numbers[index])
            operators[1] += 1

        if operators[2] > 0:
            operators[2] -= 1
            dfs(operators, index + 1, total * numbers[index])
            operators[2] += 1

        if operators[3] > 0:
            operators[3] -= 1

            if total > 0:
                dfs(operators, index + 1, (total // numbers[index]))
            else:
                dfs(operators, index + 1, (-1 * total // numbers[index]) * -1)

            operators[3] += 1

        return

    dfs(commands, 1, numbers[0])

    return ans


if __name__ == "__main__":
    result = solution()
    print(result)
