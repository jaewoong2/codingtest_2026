# https://school.programmers.co.kr/learn/courses/30/lessons/81302?utm_source=chatgpt.com

# [
#     ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
# ]
#
# [1, 0, 1, 1, 1]


# i, j를 모두 돌면서 맨해튼거리가 2인 애들 중에서 거리두기가 통과하는지 안하는지를 확인 하는 문제 로 갑시다
# 맨해튼 거리 계산
# 거리두기 통과 여부 확인 로직 (위2, 아래2, 왼2, 오2, 대각1*4)


def get_candidates(row, col, n, m, places):
    import collections

    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    visited = set()

    is_blocked = False

    queue = collections.deque()
    queue.append((row, col, 0))
    visited.add((row, col))

    while queue:
        r, c, distance = queue.popleft()

        if distance == 2:
            break

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m:
                if (nr, nc) not in visited:

                    if places[nr][nc] == "P":
                        is_blocked = True
                        return is_blocked

                    if places[nr][nc] == "O":
                        visited.add((nr, nc))
                        queue.append((nr, nc, distance + 1))

    return is_blocked


def solution(places):
    n, m = 5, 5
    results = []

    for classes in places:
        is_blocked = False

        for i in range(n):
            for j in range(m):
                if classes[i][j] == "P":
                    is_blocked = get_candidates(i, j, n, m, classes)

                if is_blocked:
                    break

            if is_blocked:
                break

        if is_blocked:
            results.append(0)
        else:
            results.append(1)

    return results
