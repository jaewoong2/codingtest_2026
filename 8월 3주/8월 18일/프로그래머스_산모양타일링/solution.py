# 공유되는 삼각형이 있는 경우
# Top이 없는 경우
# - 2
# Top이 있는 경우
# - 3

# 공유되는 삼각형이 없는 경우
# Top이 없는 경우
# - 3
# Top이 있는 경우
# - 4


# dp[1][0] = 3 # 전체
# dp[1][1] = 1 # 오른쪽 개수

# dp[2][0] = (dp[1][0] - dp[1][1]) * 4) + (dp[1][1] * 3)
# dp[2][1] = (dp[1][0])


# dp[n][0] = (dp[n - 1][0] - dp[n - 1][1] * 4) + dp[n - 1][1] * 3
# dp[n][1] = (dp[n - 1][0]) + dp[n - 1][1]


# https://school.programmers.co.kr/learn/courses/30/lessons/258705
def solution(n, tops):

    dp = [[0 for _ in range(2)] for _ in range(n)]

    if tops[0] == 1:
        dp[0][0] = 4
        dp[0][1] = 1
    else:
        dp[0][0] = 3
        dp[0][1] = 1

    for i in range(1, n):
        if tops[i] == 1:
            dp[i][0] = ((dp[i - 1][0] - dp[i - 1][1]) * 4 + dp[i - 1][1] * 3) % 10007
            dp[i][1] = (dp[i - 1][0]) % 10007
        else:
            dp[i][0] = ((dp[i - 1][0] - dp[i - 1][1]) * 3 + dp[i - 1][1] * 2) % 10007
            dp[i][1] = (dp[i - 1][0]) % 10007

    return dp[-1][0]
