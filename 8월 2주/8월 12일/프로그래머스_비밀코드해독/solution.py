# 비밀조직의 보안시스템
# 시스템 1-n | 서로 다른 정수 5개 오름 참수 비밀코드
# 비밀코드를 맞춰야함
# m 번의 시도
# 그 중 몇개가 비밀 코드에 포함되어 있는지 알려줌
# m 번의 시도 후 비밀코드로 가능한 정수 조합의 개수

# n = 10 ~ 30 / q/m = 1 ~ 10
# 모든 정수의 오름차순의 방법 [1,2,3,4,5] ~ [25,26,27,28,29,30] 30C5
# 13600 * 10 * 5 = 136

# 모든 정수의 방법 수를 찾고, 이에 대해서 쿼리/답 이 동일한것만 제출한다.

# 9 2 7 2= 4 * 63 = 252


# https://school.programmers.co.kr/learn/courses/30/lessons/388352


def combination(arr, r):
    selected = []

    def c(start, chosen):
        if len(chosen) == r:
            selected.append(chosen)
            return

        for i in range(start, len(arr)):
            c(i + 1, chosen + [arr[i]])

    c(0, [])

    return selected


def solution(n, q, ans):
    numbers = [number for number in range(1, n + 1)]
    candidates = combination(numbers, 5)
    result = 0

    for candidate in candidates:
        answer = []
        for query in q:
            count = 0
            for i in range(5):
                if query[i] in candidate:
                    count += 1

            answer.append(count)

        if answer == ans:
            result += 1

    return result
