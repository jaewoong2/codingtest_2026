def find_route(r1, c1, r2, c2):
    visited = []
    dr = 1 if r2 > r1 else -1
    dc = 1 if c2 > c1 else -1

    while r1 != r2:
        r1 += dr
        visited.append([r1, c1])

    while c1 != c2:
        c1 += dc
        visited.append([r1, c1])

    return visited


def solution(points, routes):

    paths = {}

    for route in routes:

        prev_index = route[0]
        visited = [points[prev_index - 1]]

        for current_index in route[1:]:
            r1, c1 = points[prev_index - 1]
            r2, c2 = points[current_index - 1]
            visited += find_route(r1, c1, r2, c2)
            prev_index = current_index

        for i, visit in enumerate(visited):
            key = (i, visit[0], visit[1])
            if key in paths:
                paths[key] = 1
            else:
                paths[key] = 0

    return sum(paths[x] for x in paths)
