# 상하좌우 이동 하는 함수 (r1,c1), (r2,c2)
# 회전 하는 함수 (2x1) -> (1x2) -> (2x1) -> ...
# 현재 상태 (수평/수직) 를 저장 해야 겠네..
# 90도 회전은 4방향 모두 가능
# (r1,c1), (r2,c2) 에 대한 최소 값 을 갖고 있으면 좀더 편하겠군


# https://school.programmers.co.kr/learn/courses/30/lessons/60063
def is_out(r, c, n, m):
    if 0 <= r < n and 0 <= c < m:
        return False

    return True


def rotate(maps, r1, c1, state):
    n, m = len(maps), len(maps[0])
    answer = []

    ## 수직이면 (1, 1) (2, 1) -> (1, 1) (1, 2) / (1, 0) (1, 1)
    ## 수직이면 (1, 1) (2, 1) -> (2, 0) (2, 1) / (2, 1) (2, 2)
    if state == 1:

        check = True
        # a
        if is_out(r1 + 1, c1 + 1, n, m) or maps[r1 + 1][c1 + 1] == 1:
            check = False

        if is_out(r1, c1 + 1, n, m) or maps[r1][c1 + 1] == 1:
            check = False

        if check:
            answer.append([r1, c1, r1, c1 + 1])

        check = True
        # b
        if is_out(r1 + 1, c1 - 1, n, m) or maps[r1 + 1][c1 - 1] == 1:
            check = False

        if is_out(r1, c1 - 1, n, m) or maps[r1][c1 - 1] == 1:
            check = False

        if check:
            answer.append([r1, c1 - 1, r1, c1])

        check = True
        # c
        if is_out(r1, c1 + 1, n, m) or maps[r1][c1 + 1] == 1:
            check = False

        if is_out(r1 + 1, c1 + 1, n, m) or maps[r1 + 1][c1 + 1] == 1:
            check = False

        if check:
            answer.append([r1 + 1, c1, r1 + 1, c1 + 1])

        check = True
        # d
        if is_out(r1, c1 - 1, n, m) or maps[r1][c1 - 1] == 1:
            check = False

        if is_out(r1 + 1, c1 - 1, n, m) or maps[r1 + 1][c1 - 1] == 1:
            check = False

        if check:
            answer.append([r1 + 1, c1 - 1, r1 + 1, c1])

        return answer

    # 수평이면 (1,1), (1,2) -> a(0,1), (1,1) / b(1,1), (2,1)
    # 수평이면 (1,1), (1,2) -> c(0,2), (1,2) / d(2,2), (1,2)
    if state == 0:
        check = True
        # a
        if is_out(r1 - 1, c1 + 1, n, m) or maps[r1 - 1][c1 + 1] == 1:
            check = False

        if is_out(r1 - 1, c1, n, m) or maps[r1 - 1][c1] == 1:
            check = False

        if check:
            answer.append([r1 - 1, c1, r1, c1])

        check = True
        # b
        if is_out(r1 + 1, c1 + 1, n, m) or maps[r1 + 1][c1 + 1] == 1:
            check = False

        if is_out(r1 + 1, c1, n, m) or maps[r1 + 1][c1] == 1:
            check = False

        if check:
            answer.append([r1, c1, r1 + 1, c1])

        check = True
        # c (r1, c1 + 1) 이 기준
        if is_out(r1 - 1, c1, n, m) or maps[r1 - 1][c1] == 1:
            check = False

        if is_out(r1 - 1, c1 + 1, n, m) or maps[r1 - 1][c1 + 1] == 1:
            check = False

        if check:
            answer.append([r1 - 1, c1 + 1, r1, c1 + 1])

        check = True
        # d
        if is_out(r1 + 1, c1, n, m) or maps[r1 + 1][c1] == 1:
            check = False

        if is_out(r1 + 1, c1 + 1, n, m) or maps[r1 + 1][c1 + 1] == 1:
            check = False

        if check:
            answer.append([r1, c1 + 1, r1 + 1, c1 + 1])

        return answer


def bfs(maps):
    import collections

    n, m = len(maps), len(maps[0])

    queue = collections.deque()

    visited = {}

    # r1,c1,r2,c2,상태
    queue.append((0, 0, 0, 1, 0))
    visited[(0, 0, 0, 1)] = 0

    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    while queue:
        r1, c1, r2, c2, state = queue.popleft()

        for dr, dc in moves:
            nr1, nc1, nr2, nc2 = r1 + dr, c1 + dc, r2 + dr, c2 + dc

            if 0 <= nr1 < n and 0 <= nc1 < m and 0 <= nr2 < n and 0 <= nc2 < m:
                if maps[nr1][nc1] == 1 or maps[nr2][nc2] == 1:
                    continue

                if (nr1, nc1, nr2, nc2) not in visited:
                    visited[(nr1, nc1, nr2, nc2)] = visited[(r1, c1, r2, c2)] + 1
                    queue.append((nr1, nc1, nr2, nc2, state))

                elif visited[(nr1, nc1, nr2, nc2)] > visited[(r1, c1, r2, c2)] + 1:
                    visited[(nr1, nc1, nr2, nc2)] = visited[(r1, c1, r2, c2)] + 1
                    queue.append((nr1, nc1, nr2, nc2, state))

        for nr1, nc1, nr2, nc2 in rotate(maps, r1, c1, state):
            next_state = (state + 1) % 2

            if (nr1, nc1, nr2, nc2) not in visited:
                visited[(nr1, nc1, nr2, nc2)] = visited[(r1, c1, r2, c2)] + 1
                queue.append((nr1, nc1, nr2, nc2, next_state))

            elif visited[(nr1, nc1, nr2, nc2)] > visited[(r1, c1, r2, c2)] + 1:
                visited[(nr1, nc1, nr2, nc2)] = visited[(r1, c1, r2, c2)] + 1
                queue.append((nr1, nc1, nr2, nc2, next_state))

    minimum = float("INF")

    if (n - 1, m - 2, n - 1, m - 1) in visited:
        minimum = min(visited[(n - 1, m - 2, n - 1, m - 1)], minimum)

    if (n - 2, m - 1, n - 1, m - 1) in visited:
        minimum = min(visited[(n - 2, m - 1, n - 1, m - 1)], minimum)

    return minimum


def solution(board):
    return bfs(board)
