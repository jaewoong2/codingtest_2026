import sys

# ==============================================================================
# [코딩테스트 파이썬 템플릿]
# 1. 빠른 입출력 설정
# 2. 재귀 깊이 제한 해제 (DFS/트리 문제 시 필수)
# 3. 로컬 테스트용 input.txt 자동 연동 (원할 때 주석 해제하여 사용 가능)
# ==============================================================================

# sys.setrecursionlimit(10**6) # 재귀 문제 풀 때 주석 해제

input = sys.stdin.readline

def solution():
    # ---------------------------------------------------------
    # 예시 문제: N개의 정수가 주어질 때 합계와 평균, 최대/최소 구하기
    # ---------------------------------------------------------
    
    # 1. 입력 받기
    try:
        line1 = input().strip()
        if not line1:
            return
        n = int(line1)
        numbers = list(map(int, input().split()))
    except ValueError:
        print("입력 형식이 올바르지 않습니다.")
        return

    # 2. 알고리즘 로직 처리
    total_sum = sum(numbers)
    average = total_sum / n
    max_val = max(numbers)
    min_val = min(numbers)

    # 3. 결과 출력
    print(f"개수: {n}")
    print(f"합계: {total_sum}")
    print(f"평균: {average:.2f}")
    print(f"최댓값: {max_val}, 최솟값: {min_val}")

if __name__ == "__main__":
    solution()
