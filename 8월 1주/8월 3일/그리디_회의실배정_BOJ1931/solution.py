import sys
import os

if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")):
    sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

input = sys.stdin.readline

## 문제 해결 방법
# -> 1. 끝나는 시간이 빠르게 오게끔 정렬
# -> 2. 그 끝나는 시간 보다 큰 시작 시간들 중, 가장 빠르게 끝나는 시간이 오게끔 정렬
# -> 3. 모든 배열 탐색 종료
# -> 4. 결과값 반환


def solution():
    n = int(input())
    arrs = sorted(
        [list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1]
    )
    now_time = 0
    result = 0
    for start, end in arrs:
        if start < now_time:  # 시작시간이 끝나는 시간이 되는 경우
            continue

        now_time = end
        result += 1

    return result


if __name__ == "__main__":
    response = solution()
    print(response)
