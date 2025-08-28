# 문제: 미로에서 특정 값 찾기

# N×M 격자가 주어진다.
# 각 칸에는 0~9 사이의 숫자가 있다.
# 시작점 (0,0)에서 출발하여 상하좌우로 이동할 수 있다.
# 목적지는 (N-1, M-1)이며, 총 이동한 칸들의 숫자를 합한 값이 K 이하이어야 한다.
# 질문: 도착점까지 도달 가능한 경로가 있는가?

# 입력 예시
# 3 3 7
# 1 2 3
# 0 1 2
# 2 1 1

# 3×3 격자, 합 제한 K=7

n = 3
m = 3
k = 7

grid = [
    [1, 2, 3],
    [0, 1, 2],
    [2, 1, 1]
]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*m for _ in range(n)]

def dfs(x, y, total):
    # 범위 벗어나거나 방문했으면 종료
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y]:
        return False
    
    total += grid[x][y]
    # 합이 K를 넘으면 더 이상 진행 X
    if total > k:
        return False
    
    # 도착점 도달
    if x == n-1 and y == m-1:
        return True
    
    visited[x][y] = True
    for i in range(4):
        if dfs(x + dx[i], y + dy[i], total):
            return True
    visited[x][y] = False  # 다른 경로를 위해 방문 초기화
    return False

result = dfs(0, 0, 0)
print(result)  # True
