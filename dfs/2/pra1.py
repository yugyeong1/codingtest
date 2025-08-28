# 📌 문제 2. 단지 번호 붙이기 (BOJ 2667 스타일)

# N×N 격자에서 1은 집이 있고, 0은 집이 없는 칸이다.
# 집이 상하좌우로 연결되면 하나의 단지를 이룬다.
# 총 단지 수와 각 단지 내 집의 수를 오름차순 정렬하여 출력하라.

# 입력 예시
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000


n = 7
graph = [
            [0, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0 ,1],
            [1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0],
        ]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    cnt = 1
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            cnt = cnt + dfs(x+dx[i], y+dy[i])
        return cnt
    return 0

# 1로 연결돼있는 영역의 수를 구함
result = 0
house_count = []
for i in range(n):
    for j in range(n):
        cnt = dfs(i, j)
        if cnt > 0:
            result += 1
            house_count.append(cnt)
            
house_count.sort()            
print(result)
print(house_count)

