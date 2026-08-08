def bfs(array, target):
    import collections
    
    queue = collections.deque()
    
    queue.append((0, array[0]))
    queue.append((0, -array[0]))
    answer = 0
    
    while len(queue) > 0:
        index, value = queue.popleft()
        
        if len(array) == index + 1:
            if value == target:
                answer += 1
            continue
        
        queue.append((index + 1, value + array[index + 1]))
        queue.append((index + 1, value - array[index + 1]))
    
    return answer

def solution(numbers, target):
    return bfs(numbers, target)
