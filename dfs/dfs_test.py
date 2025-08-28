

n = 4
m = 5

graph = [
            [0, 0, 1, 1, 0],         
            [0, 0, 0, 1, 1],         
            [1, 1, 1, 1, 1],         
            [0, 0, 0, 0, 0]         
        ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
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