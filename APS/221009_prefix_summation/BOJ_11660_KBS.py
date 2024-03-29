import sys
N, M = map(int,input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[0]* (N+1) for _ in range(N+1)]                                   #좌상 한칸씩 더해서 모서리 부분 따로 계산X

for i in range (1,N+1):
    for j in range(1,N+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(DP[x2][y2]- DP[x2][y1-1]-DP[x1-1][y2]+DP[x1-1][y1-1])

