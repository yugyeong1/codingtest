
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


def bfs(x, y, height, visited, area):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if ( nx >= 0 and nx < n ) and ( ny >= 0 and ny < n ):
                if not visited[nx][ny] and area[nx][ny] > height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 0 ~ 최대 높이 까지 for문을 돌면서 현재 높이보다 높은 곳의 영역 덩어리가 몇 개인가
#                               (잠기지 않아야 하기 때문)

max_height = max(max(row) for row in area)
result = 0
for height in range(0, max_height +1):
    # 현재 높이에 대한 방문 기록 및 몇 개의 영역이 있는지 count
    visited = [[False] * n for i in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and not visited[i][j]:
                bfs(i, j, height, visited, area)
                count += 1
                
    # 현재 높이의 방문이 모두 종료되면 result에 최대 값으로 업데이트
    result = max(result, count)

print(result)