def solution(n, stages):
    n_pass = {i + 1: 0 for i in range(n + 1)}
    n_pass_with_challenge = {i + 1: 0 for i in range(n + 1)}
    answer = []

    # 통과율 / 도전+통과 계산
    for stage in stages:
        n_pass_with_challenge[stage] += 1
        for i in range(1, stage):
            n_pass[i] += 1
            n_pass_with_challenge[i] += 1

    for i in range(1, n + 1):
        # 통과한사람/도전+통과 = (성공률, 스테이지)
        if n_pass_with_challenge[i] > 0:
            answer.append((n_pass[i] / n_pass_with_challenge[i], i))
        else:
            answer.append((1, i))

    answer.sort(key=lambda x: x[0])

    return [x[1] for x in answer]
