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


def permuation(arr, r):
    selected = []

    def backtracking(chosen, visited):
        if len(chosen) == r:
            selected.append(chosen)
            return

        for i in range(len(arr)):
            if i not in visited:
                visited.add(i)
                backtracking(chosen + [arr[i]], visited)
                visited.remove(i)

        return

    visited = set()
    backtracking([], visited)

    return selected


def calcuator(index, arr, commands, total):
    if index == len(arr):
        return total

    temp = total
    if commands[index - 1] == "+":
        temp = total + arr[index]

    if commands[index - 1] == "-":
        temp = total - arr[index]

    if commands[index - 1] == "*":
        temp = total * arr[index]

    if commands[index - 1] == "/":
        if total > 0:
            temp = total // arr[index]
        else:
            temp = ((total) * -1 // arr[index]) * -1

    return calcuator(index + 1, arr, commands, temp)


def solution():
    n = int(input())
    numbers = [x for x in map(int, input().split())]
    commands = [x for x in map(int, input().split())]
    c = []

    for i in range(4):
        for _ in range(commands[i]):
            if i == 0:
                c.append("+")
            if i == 1:
                c.append("-")
            if i == 2:
                c.append("*")
            if i == 3:
                c.append("/")

    candidates = permuation(c, n - 1)

    ans = [-1 * int(1e20), int(1e20)]
    visited = set()

    for candidate in candidates:
        txt = "".join(candidate)
        if txt not in visited:
            visited.add(txt)
            value = calcuator(1, numbers, candidate, numbers[0])

            ans[0] = max(ans[0], value)
            ans[1] = min(ans[1], value)

    return ans


if __name__ == "__main__":
    result = solution()
    print(result)
