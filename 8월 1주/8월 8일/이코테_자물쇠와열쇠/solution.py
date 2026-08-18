def expand(array, size):
    length = len(array) + size * 2
    new_array = [[0 for _ in range(length)] for _ in range(length)] 
    
    for i in range(len(array)):
        for j in range(len(array)):
            value = array[i][j]
            new_array[i + size][j + size] = value
            
    return new_array

def rotate(array):
    new_array = [[col for col in row] for row in array]
    for i in range(len(array)):
        for j in range(len(array)):
            new_array[i][j] = array[len(array) - j - 1][i]
    
    return new_array

def move2(row, col, lock, key, n):
    m = len(key)
    new_lock = [[x for x in row] for row in lock]
    
    for i in range(m):
        for j in range(m):
            if new_lock[row + i][col + j] == 0:
                new_lock[row + i][col + j] = key[i][j]
            elif new_lock[row + i][col + j] == 1 and key[i][j] == 1:
                # 돌기가 중복되면 안되게 막기
                new_lock[row + i][col + j] = int(1e10)
                
    array = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(new_lock[m + i][m + j])
        
        array.append(row)
    
    return array
    
def move(key, lock, real_array_length):
    n, m = len(lock), len(key)
    answer = False
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            arr = move2(i, j, lock, key, real_array_length)
            total = 0
            for row in arr:
                total += sum(row)
            
            if total == real_array_length ** 2:
                answer = True
                break
            
    return answer

def solution(key, lock):
    new_lock = expand(lock, len(key))
    
    for _ in range(4):
        key = rotate(key)
        if move(key, new_lock, len(lock)):
            return True
    
    return False
