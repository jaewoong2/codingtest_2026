import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline


# 모험가 길드에 N명에 대해서 공포도를 측정 했음
# 공포도가 높은 모험가는 상황 대처 못함
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 모험이 가능
# "최대 몇개의 모험가 그룹" 을 만들 수 있는지.
# 2 3 1 2 2
# -> Idea) 최소 공포도를 가진 사람 먼저 내보내면 최대 아닌가?
# -> 반례생각) 없는거같음
# -> 예제) 1 / 2 2  -> 2개


def solution():
    n = int(input())
    users = sorted([x for x in map(int, input().split())])

    groups = 0
    length = 0

    for fear in users:
        length += 1
        if length >= fear:
            groups += 1
            length = 0

    return groups


if __name__ == "__main__":
    result = solution()
    print(result)
