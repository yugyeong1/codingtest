
# N×N 땅이 주어진다. 각 칸에는 높이가 적혀 있다.
# 비가 와서 특정 높이 h 이하의 지역은 잠긴다.
# 잠기지 않은 지역들 중에서 연결된 영역의 개수를 구하라.
# 출력: 모든 h에 대해 가능한 영역 개수 중 최대값
from collections import deque

n = 5
area = [
            [6, 8, 2, 6, 2], 
            [3, 2, 3, 4, 6],
            [6, 7, 3, 3, 2],
            [7, 2, 5, 3, 6],
            [8, 9, 5, 2, 7]
        ]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, height, visited, area):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < n):
                if area[nx][ny] > height and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 0 ~ 최대 높이까지 for문을 돌면서 현재 높이보다 높은 영역이 몇 개 있는지 확인
# 그리고 그 중 가장 큰 값을 리턴
max_length = max(max(row) for row in area)
result = 0

for height in range(0, max_length + 1):
    visited = [[False] * n for i in range(n)]
    count = 0    
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j] > height:
                dfs(i, j, height, visited, area)
                count += 1
                
    result = max(count, result)

print(result)