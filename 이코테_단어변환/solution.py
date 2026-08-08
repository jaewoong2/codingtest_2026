def check(word1, word2):
    count = 0
    
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    
    if count == 1:
        return True
    
    if count > 1:
        return False

# 가장 짧은 변환 과정
def bfs(start, target, words):
    import collections
    
    queue = collections.deque()
    queue.append((start, 0))
    
    
    while len(queue) > 0:
        curr, count = queue.popleft()
        
        
        if count >= len(words):
            return 0
        
        if curr == target:
            return count
        
        for word in words:
            if check(word, curr):
                queue.append((word, count + 1))
        
    return 0


def solution(begin, target, words):
    return bfs(begin, target, words)
