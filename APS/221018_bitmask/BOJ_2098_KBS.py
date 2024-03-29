N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] *(1 << N) for _ in range(N)]
for g in range(N):
    if arr[0][g]:
        DP[g][1 << g] = arr[0][g]
            
for i in range(1, 1 <<N):
    for j in range(1, N):
        if not DP[j][i]:
            continue
        for k in range(1, N):
            if arr[j][k] and not(i & 1 << k):
                if DP[k][i | 1 << k] == 0:
                    DP[k][i | 1 << k] = arr[j][k] + DP[j][i]
                else:
                    if DP[k][i | 1 << k] > arr[j][k] + DP[j][i]:
                        DP[k][i | 1 << k] = arr[j][k] + DP[j][i]

ans = 1e8
for h in range(1,N):
    temp = DP[h][(1<<N)-2] + arr[h][0]
    if DP[h][(1<<N)-2]and arr[h][0] and temp < ans:
        ans = DP[h][(1<<N)-2] + arr[h][0]
print(ans)

