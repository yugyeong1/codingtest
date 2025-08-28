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


visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, total):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    total += grid[x][y]
    
    # 합 제한을 넘어갈 시 false 리턴
    if total > k:
        return False
    
    # 도착지점 도착
    if x == n-1 and y == m-1:
        return True
    
    visited[x][y] == True
    
    for i in range(4):
        if dfs( x + dx[i], y + dy[i] ,total) == True:
            return True
        
    visited[x][y] = False
    return False

result = dfs(0, 0, 0)
print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    

