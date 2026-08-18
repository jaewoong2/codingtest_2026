# 순서대로 n개의 퍼즐을 제한 시간 내에 풀어야함
# 퍼즐은 난이도와 소요 시간이 정해져있음
# 숙련도에 다라 퍼즐을 풀때 틀리는 횟수가 바뀌게 됨
# diff, time_cur, time_prev, level

# diff <= level ==> time_cur
# diff > level ==> (diff - level + time_prev) * time_cur + time_cur

# 이전버전을 다시 풀때는 이전 퍼즐의 난이도에 상관 없이 풀면 time_cur만큼 만 걸림 ㅇㅇ
# (diff - level) * time_cur 이 걸리는게 아니라

# 제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 정수로 return


# https://school.programmers.co.kr/learn/courses/30/lessons/340212?utm_source=chatgpt.com#


def solution(diffs, times, limit):
    # time_prevs[i] => i-1 다시 푸는 시간
    time_prevs = [0]

    for i, time in enumerate(times):
        time_prevs.append(time)

    result = max(diffs)
    left, right = 0, max(diffs)

    while left <= right:
        time = 0
        level = (left + right) // 2

        for i, diff in enumerate(diffs):
            if diff <= level:
                time = time + times[i]
            else:
                time = time + ((diff - level) * (times[i] + time_prevs[i])) + times[i]

        # 통과하면 갱신 / right를 줄인다
        if time <= limit:
            result = min(result, level)
            right = level - 1
        else:
            left = level + 1

    # 난이도, 소요 시간은 모두 양의 정수며, 숙련도도 양의 정수여야 합니다.... (이거 틀림 ㅡ.ㅡ)
    return max(result, 1)
