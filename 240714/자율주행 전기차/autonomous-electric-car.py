import sys
from collections import deque
input = sys.stdin.readline
dx,dy = [0,-1,0,1],[-1,0,1,0]
n,m,c = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
x_now,y_now = map(int,input().split())
x_now,y_now = x_now-1,y_now-1
location={}

for _ in range(m):
    x_s,y_s,x_e,y_e = map(int, input().split())
    q = deque()
    q.append((x_s-1,y_s-1,0))
    visit = [[False]*n for _ in range(n)]
    visit[x_s-1][y_s-1] = True
    while q:
        x, y, d = q.popleft()
        if x==x_e-1 and y==y_e-1:
            location[(x_s-1,y_s-1)] = (x_e-1,y_e-1,d)
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and graph[nx][ny]==0:
                visit[nx][ny] = True
                q.append((nx,ny,d+1))

for _ in range(m):
    # 승객 거리 계산
    q = deque()
    q.append((x_now,y_now,0))
    visit = [[False]*n for _ in range(n)]
    visit[x_now][y_now] = True
    passenger = []
    while q:
        x,y,d = q.popleft()
        if (x,y) in location:
            passenger.append((x,y,d))
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and graph[nx][ny]==0:
                q.append((nx,ny,d+1))
                visit[nx][ny] = True
    if not passenger:
        print(-1)
        break
    # 승객 정렬 (거리, x, y)
    passenger = sorted(passenger, key = lambda x:(x[2],x[0],x[1]))
    x_p, y_p, d = passenger[0][0],passenger[0][1],passenger[0][2]
    # 아무도 못 태우는 경우
    if c-d<0:
        print(-1)
        break
    x_now, y_now, c = x_p, y_p, c-d
    # 승객 위치에서 목적지 거리 계산
    if c-location[(x_now,y_now)][2]<0:
        print(-1)
        break
    ax, ay = x_now, y_now
    x_now, y_now, c = location[(x_now,y_now)][0],location[(x_now,y_now)][1],c+location[(x_now,y_now)][2]
    del location[(ax,ay)]

else: print(c)