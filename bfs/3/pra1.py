# 📌 예시 문제 : 미로 탐색 (Shortest Path in a Maze)

# N×M 크기의 미로가 주어진다.

# 1은 이동할 수 있는 칸,

# 0은 벽(이동 불가)이다.

# 당신은 (0,0) 위치에서 시작해서 (N-1, M-1) 위치까지 도달하려고 한다.
# 한 번에 상하좌우로 이동할 수 있으며, 벽을 통과할 수는 없다.

# (0,0)에서 (N-1, M-1)까지의 최단 경로 길이를 BFS로 구하라.
# 만약 도달할 수 없다면 -1을 출력하라.


from collections import deque

n = 5
m = 6
graph = [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1 ,0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 1 ,1],
        ]



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, graph):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]                


# 최단 경로 : bfs
result = dfs(0, 0, graph)

print(result)

