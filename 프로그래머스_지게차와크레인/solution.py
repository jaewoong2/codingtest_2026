# 알파벳이 하나만 -> 지게차 -> 바깥 0 에서 접근 가능 한경우
# 알파벳이 2개인 경우 -> 크레인 -> 그냥 해당 문자열을 빼버림
# 바깥 0 을 extend 하는게 편해보임


def extend(maps):
    n, m = len(maps), len(maps[0])
    temp = []

    temp.append([0 for _ in range(m + 2)])

    for i in range(n):
        row = [0]
        for j in range(m):
            row.append(maps[i][j])
        row.append(0)

        temp.append(row)

    temp.append([0 for _ in range(m + 2)])

    return temp


def search(row, col, maps, visited, target):
    from collections import deque

    n, m = len(maps), len(maps[0])

    queue = deque()

    queue.append((row, col))

    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    arr = []
    while queue:
        r, c = queue.popleft()

        if maps[r][c] == target:
            arr.append((r, c))
            continue

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m:
                if (nr, nc) not in visited:
                    if maps[nr][nc] == 0 or maps[nr][nc] == target:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

    return arr


def search_from_outside(maps, target):
    n, m = len(maps), len(maps[0])
    visited = set()

    visited.add((0, 0))
    value = search(0, 0, maps, visited, target)

    if value:
        for row, col in value:
            maps[row][col] = 0


def solution(storage, requests):
    storage = extend(storage)
    keys = {r[0]: [] for r in requests}

    for request in requests:
        for i in range(len(storage)):
            for j in range(len(storage[i])):
                if request[0] == storage[i][j]:
                    keys[request[0]].append((i, j))

    for request in requests:
        if len(request) == 1:
            search_from_outside(storage, request)

        if len(request) == 2 and len(keys[request[0]]) > 0:
            for r, c in keys[request[0]]:
                storage[r][c] = 0
                keys[request[0]] = []
    answer = 0

    for r in storage:
        for c in r:
            if c != 0:
                answer += 1

    return answer
