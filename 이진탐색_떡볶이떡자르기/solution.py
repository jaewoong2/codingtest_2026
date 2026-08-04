import sys

# ==============================================================================
# 꿀팁: 파이썬 코드 자체에서 같은 폴더의 input.txt가 있으면 자동으로 읽게 만드는 코드
# (백준/프로그래머스에 제출할 때도 이 코드를 그대로 제출해도 자동으로 표준입력을 받아 정상 동작합니다!)
# ==============================================================================
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

# 최소 target 만큼 sum이 되도록 해야함
# 예를 들어 가장 길게 가져가게 하려면 값은 0
# 예를 들어 가장 작게 가져가게 하려면 값은 max(array) ~ 무한대
# 계속해서 중간값을 찾으면서, 절단기를 뺀만큼의 합이 target 보다 크거나 같도록 한다 (갱신)


def solution():
    n, target = map(int, input().split())
    array = [x for x in map(int, input().split())]

    def binary_search():
        result = 0
        minium, maximum = 0, max(array)

        # while minimum < maximum: # 경우는, maximum 을 정답에서 제외하는 경우.
        while minium <= maximum:
            mid = (minium + maximum) // 2
            value = sum([max(x - mid, 0) for x in array])

            if value >= target:
                # 절단기의 높이를 더 키워야 함
                result = max(result, mid)
                minium = mid + 1
            else:
                # 절단기의 높이를 더 줄여야함
                maximum = mid - 1
                # maximum = mid # 다음 탐색에서 mid를 다시 볼 필요가 없습니다.

        return result

    return binary_search()


if __name__ == "__main__":
    result = solution()
    print(result)
