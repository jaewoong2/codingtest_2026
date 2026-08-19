# 1~n개
# 주사위의 면은 1~6
# A가 승리할 확률이 가장 높아지도록 주사위를 가져가려함
# 모든경우의 수에 대해서 실패 결과


# 주사위를 nC2
# 1. 주사위 조합에서 a~f 까지 나오는 모든 경우의 수 를 구함
# 1. total = (1~n // 2) * 6개중에서 1개를 선택하는 경우의수
# 2. sum(a_totals) > sum(b_totals)


# https://school.programmers.co.kr/learn/courses/30/lessons/258709
def combinations(arr, r):
    chosen = []

    def c(start, selected):
        if len(selected) == r:
            chosen.append(selected)
            return

        for i in range(start, len(arr)):
            c(i + 1, selected + [arr[i]])

    c(0, [])

    return chosen


def get_sums(dices):
    sums = []

    def dfs(depth, cur_sum):
        if len(dices) == depth:
            sums.append(cur_sum)
            return

        for dice in dices[depth]:
            dfs(depth + 1, cur_sum + dice)

    dfs(0, 0)

    return sums


def total(dices):
    totals = []

    pivot = dices[0]

    if len(dices) == 1:
        return dices[0]

    for left_value in pivot:
        for right_value in total(dices[1:]):
            totals.append(left_value + right_value)

    return totals


# arr에서 pivot 보다 더 큰 값을 갖는 인덱스를 반환한다
# arr은 정렬이 되어 있다.


# lower_bound, upper_bound 에 대해서 조금 이해도를 높여야 할것 같음.
def binary_search(pivot, arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # 타겟이 중앙 보다 작으면
        # 같다 조건을 안하면, 동일한 숫자들이 [1,1,1,1,1,1,2,2,2,2,2,2] 있을때 정확한 위치를 못찾는다
        if pivot <= arr[mid]:
            right = mid - 1
        elif pivot > arr[mid]:
            left = mid + 1

    return left  # arr[:left] => pivot 보다 작음 // arr[left:] -> pivot 보다큼


def solution(dice):
    numbers = [x for x in range(len(dice))]

    a_choices = sorted(combinations(numbers, len(dice) // 2))

    maximum = -1
    answer = []
    cache = {}

    for a_choice in a_choices:
        b_choice = set(numbers) - set(a_choice)

        a_win = 0
        b_win = 0

        a_values = get_sums([dice[index] for index in a_choice])
        b_values = sorted(get_sums([dice[index] for index in b_choice]))

        cache = {}

        for a_value in a_values:
            if a_value in cache:
                a_win += cache[a_value]
            else:
                index = binary_search(a_value, b_values)
                cache[a_value] = len(b_values[:index])
                a_win += cache[a_value]

        if maximum < a_win:
            answer = a_choice
            maximum = a_win

    return sorted([x + 1 for x in answer])
