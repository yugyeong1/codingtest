from collections import deque

# 5 x 6 행렬
n = 5
m = 6

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    print(f'queue : {queue}')
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 공간 벗어날 경우 무시
            if nx < 0 or nx >= 5 or ny < 0 or ny >= m:
                continue
            # 벽이면 무시
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]
    
graph = [ 
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
        ]

print(bfs(0, 0))
