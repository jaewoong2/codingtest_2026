def solution(n, computers):
    graphs = {}
    visited = {}
    
    for i in range(n):
        computer = computers[i] 
        graphs[i] = []
        for j in range(n):
            if i != j and computer[j] == 1:
                graphs[i].append(j)
    
    
    def dfs(node):
        for next_node in graphs[node]:
            if next_node in visited:
                continue
                
            visited[next_node] = False
            dfs(next_node)
    
    answer = 0
    for i in range(n):
        if i not in visited:
            answer += 1
            visited[i] = True
            dfs(i)
    
    return answer
