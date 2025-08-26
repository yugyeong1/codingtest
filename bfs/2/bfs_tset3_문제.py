
# N×N 땅이 주어진다. 각 칸에는 높이가 적혀 있다.
# 비가 와서 특정 높이 h 이하의 지역은 잠긴다.
# 잠기지 않은 지역들 중에서 연결된 영역의 개수를 구하라.
# 출력: 모든 h에 대해 가능한 영역 개수 중 최대값

from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]  

def bfs(x, y, h, visited, area):
    n = len(area)
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and area[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

n = 5
area = [
            [6, 8, 2, 6, 2], 
            [3, 2, 3, 4, 6],
            [6, 7, 3, 3, 2],
            [7, 2, 5, 3, 6],
            [8, 9, 5, 2, 7]
        ]

max_height = max(max(row) for row in area)
result = 0

for h in range(0, max_height+1):  # 모든 물 높이 시도
    visited = [[False]*n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited, area)
                count += 1  # 한 영역 탐색 후 영역 개수 +1
    
    result = max(result, count)  # 최대 안전 영역 개수 갱신

print(result)
