from collections import deque

n = 5
m = 6

# 상하좌우 계산 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [ 
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
        ]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 먼저 범위 벗어나는지 확인
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 6:
                continue
            
            # 해당 좌표 값이 벽인지 확인
            if graph[nx][ny] == 0:
                continue
            
            # 만약 길이라면 다음 좌표로 이동하기 위해 queue에 해당 값 넣어줌
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

result = bfs(0, 0)
print(result)