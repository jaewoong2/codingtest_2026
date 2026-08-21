# [PCCP 기출문제] 4번 / 수레 움직이기
# https://school.programmers.co.kr/learn/courses/30/lessons/250134

import sys

# ==========================================
# 1. 정석 풀이 (동시 이동 백트래킹 DFS)
# ==========================================
def solution(maze):
    n, m = len(maze), len(maze[0])
    
    # 시작 위치 탐색
    # 1: 빨강 시작, 2: 파랑 시작, 3: 빨강 도착, 4: 파랑 도착, 5: 벽
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rx, ry = i, j
            elif maze[i][j] == 2:
                bx, by = i, j

    visited_r = [[False] * m for _ in range(n)]
    visited_b = [[False] * m for _ in range(n)]
    visited_r[rx][ry] = True
    visited_b[bx][by] = True

    ans = float('inf')
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(rx, ry, bx, by, turns):
        nonlocal ans
        r_end = (maze[rx][ry] == 3)
        b_end = (maze[bx][by] == 4)

        # 1. 종료 조건: 두 수레 모두 도착 칸에 도달한 경우
        if r_end and b_end:
            ans = min(ans, turns)
            return

        # 가지치기: 이미 구한 최솟값 이상이면 추가 탐색 불필요
        if turns >= ans:
            return

        # 2. 빨간 수레 이동 후보군 생성
        r_cands = []
        if r_end:
            r_cands.append((rx, ry))  # 이미 도착했다면 제자리에 고정
        else:
            for i in range(4):
                nr, nc = rx + dr[i], ry + dc[i]
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5 and not visited_r[nr][nc]:
                    r_cands.append((nr, nc))

        # 3. 파란 수레 이동 후보군 생성
        b_cands = []
        if b_end:
            b_cands.append((bx, by))  # 이미 도착했다면 제자리에 고정
        else:
            for i in range(4):
                nr, nc = bx + dr[i], by + dc[i]
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5 and not visited_b[nr][nc]:
                    b_cands.append((nr, nc))

        # 4. 두 수레의 동시 이동 조합 탐색
        for nrx, nry in r_cands:
            for nbx, nby in b_cands:
                # 조건 A: 두 수레가 같은 칸으로 동시에 이동 불가
                if nrx == nbx and nry == nby:
                    continue
                # 조건 B: 두 수레가 서로 자리를 맞바꾸며 이동 불가 (크로스 스왑)
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                    continue

                # 이동 처리 (도착지에 이미 있는 수레는 방문 처리 변경 안 함)
                if not r_end:
                    visited_r[nrx][nry] = True
                if not b_end:
                    visited_b[nbx][nby] = True

                dfs(nrx, nry, nbx, nby, turns + 1)

                # 백트래킹 복원
                if not r_end:
                    visited_r[nrx][nry] = False
                if not b_end:
                    visited_b[nbx][nby] = False

    dfs(rx, ry, bx, by, 0)
    return ans if ans != float('inf') else 0
