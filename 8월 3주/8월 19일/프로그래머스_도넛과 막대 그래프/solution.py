from collections import deque

# 이 그래프들과 무관한 정점을 하나 생성한 뒤, 각 도넛 모양 그래프, 막대 모양 그래프,
# 8자 모양 그래프의 임의의 정점 하나로 향하는 간선들을 연결했습니다.


# indegree = 0 인 경우에 대해서 모두 탐색
# 탐색시 제대로 생성 되면 -> 그녀석이 정점


def check_graph(graphs, start):
    # Cycle 발생
    # n = 1 인 경우, edge = 1 node = 1
    # n인 경우, edge = n node = n

    queue = deque()
    queue.append(start)

    visited = set()
    visited_node = set()

    is_cycle = False

    visited_node.add(start)

    while queue:
        current = queue.popleft()

        for next_node in graphs[current]:
            if (current, next_node) in visited:
                is_cycle = True
                continue

            visited_node.add(next_node)
            visited.add((current, next_node))
            queue.append(next_node)

    return visited, visited_node, is_cycle


def check_stick(graphs, start):
    # Cycle 발생 안함
    # n = 1 인 경우, edge = 0 node = 1
    # n인 경우, edge = n - 1 node = n
    return


def check_eight(graphs, start):
    # Cycle 발생
    # n = 1 인 경우, edge = 4 node = 3
    # n인 경우, edge = 2n + 2 node = 2n + 1
    return


# https://school.programmers.co.kr/learn/courses/30/lessons/258711
def solution(edges):
    graphs = {}
    indegress = {}
    answer = []

    for a, b in edges:
        if a in graphs:
            graphs[a].append(b)
        else:
            graphs[a] = [b]

        if b not in graphs:
            graphs[b] = []

        if b not in indegress:
            indegress[b] = 1
        else:
            indegress[b] += 1

        if a not in indegress:
            indegress[a] = 0

    candidates = [key for key in indegress if indegress[key] == 0]

    for key in candidates:
        temp = [key, 0, 0, 0]

        nodes = []
        temp[0] = key

        for node in graphs[key]:
            nodes.append(node)

        for node in nodes:
            edge_, node_, is_cycle = check_graph(graphs, node)

            if len(node_) == len(edge_) and is_cycle:
                # 도넛
                temp[1] += 1

            # elif len(node_) == len(edge_) + 1 and not is_cycle:
            # 막대

            elif len(node_) + 1 == len(edge_) and is_cycle:
                temp[3] += 1

            else:
                temp[2] += 1

        answer.append(temp)

    return max(answer, key=lambda x: sum(x[1:]))
