def solution(land):
    n, m = len(land), len(land[0])

    # 시추관을 수직으로 단 하나만 뚫을 수 있는 상태일 때
    # 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고함
    # 1~m 까지의 모든 경우를 모두다 구하면 되려나?

    # m * (n * m) = 125,000,000
    # 어차피 가로 m만큼 선택 / (0, m) ~ (n, m) 에서 bfs 이기 때문에 괜찮으려나?
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def bfs(r, c, count):
        visited = set()
        queue = []

        queue.append((r, c))
        visited.add((r, c))

        while queue:
            r, c = queue.pop()

            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    if land[nr][nc] == 1 and (nr, nc) not in visited:
                        land[nr][nc] = count
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return len(visited)

    oils = {}
    count = 2

    # 땅 그룹핑
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                land[i][j] = count
                visited = bfs(i, j, count)
                oils[count] = visited
                count += 1

    answer = 0
    for j in range(m):
        seen = set()  # 해당 열에서 이미 확인한 덩어리 번호
        col_oil = 0
        for i in range(n):
            key = land[i][j]
            if key > 1 and key not in seen:
                seen.add(key)
                col_oil += oils[key]
        answer = max(answer, col_oil)

    return answer


# 다음 문제를 위한 체크포인트
# 반복문 내부에서 [0] * K와 같이 동적으로 변하는 크기
# K
# K의 배열을 반복 생성하거나 sum()을 호출하고 있지 않은지 체크해 보세요.
# K
# K가 최대 격자 크기만큼 커질 수 있는 문제에서는
# M
# ×
# K
# M×K 복잡도가 숨겨진 시간 초과의 주원인이 됩니다.
# 부분 상태를 모을 때는 항상 **"실제로 이번 단계에서 등장할 수 있는 최대 원소 수"**에 맞춰 set()이나 해시맵을 활용하는 습관을 들이면 좋습니다.
