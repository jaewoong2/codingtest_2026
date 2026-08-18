# 온라인게임을 운영
# 이용하는 사람이 m명이 늘어날때마다 1대
# n x m명 이상 (n + 1) x m명 미만 => 최소 n대의 서버는 있어야함
# 한번 증설한 서버 n대는 k시간동안 운영하고 반납함
# 게임을 하기 위해 서버를 최소 몇 번 증설해야 하는지 알고 싶음

# 이용자수와 서버의 개수를 계속 확인 해가면서
# 서버의 수가 player // m <= 서버 <= (player // m) + 1 인지 확인해서 맞으면 -> 시간 흐름
# 서버의 수가 player // m <= 서버 <= (player // m) + 1 인지 확인해서 아니면 -> 서버 추가


# https://school.programmers.co.kr/learn/courses/30/lessons/389479?utm_source=chatgpt.com


def solution2(players, m, k):
    # servers[i] = i시간대에 서버의 개수
    servers = [0 for _ in range(len(players))]
    answer = 0

    # 시간에 맞춰서 서버를 추가한다.
    for time, player in enumerate(players):
        current_server = servers[time]
        minimum_server_number = player // m

        if minimum_server_number > current_server:
            added = minimum_server_number - current_server
            answer += added

            # time ~ time + k 만큼 서버 개수를 채운다
            # 근데 time + k 가 전체 len(players) 보다 클 수 있으니 막자
            for i in range(time, min(len(players), time + k)):
                servers[i] += added

    return answer


def bfs(players, m, k):
    from collections import deque

    queue = deque()

    # 서버들
    # 증설 횟수
    # 근데 해당 서버가 언제 추가 되었는지 확인도 해야 하는거 같은데.
    queue.append([[], 0, 0])

    answer = 0

    while queue:
        servers, time, count = queue.popleft()
        n = len(servers)

        if time >= len(players):
            return count

        if players[time] // m > n:
            queue.append([servers + [k], time, count + 1])
        else:
            for i in range(n):
                servers[i] -= 1
            queue.append([[x for x in servers if x > 0], time + 1, count])


def solution(players, m, k):
    return solution2(players, m, k)
