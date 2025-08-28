# 문제 4️⃣ : 배추 밭 군락

# 격자 N×M에서 1은 배추, 0은 빈 칸.

# 상하좌우 연결된 배추는 하나의 군락

# 목표: 군락 수 출력

# 입력
n = 5
m = 5
grid = [
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if grid[x][y] == 1:
        grid[x][y] = 0
        
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False
        

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
        
print(result)