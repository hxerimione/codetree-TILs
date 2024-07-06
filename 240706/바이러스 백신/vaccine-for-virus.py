import sys
from itertools import combinations 
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = []
dx, dy = [-1,0,1,0],[0,-1,0,1]
for _ in range(N):
    graph.append(list(map(int,input().split())))
new_graph = [[-1]* N for _ in range(N)]
hospital = []
answer=[]
for i in range(N):
    for j in range(N):
        #병원 찾기
        if graph[i][j] == 2:
            hospital.append((i,j))
hospital_list = list(combinations(hospital,M))
for hlist in hospital_list:
    new_graph = [[-1]* N for _ in range(N)]
    q=deque()
    # 병원 추가
    for h in hlist :
        a,b = h
        h = a,b,0
        q.append(h)
    while q:
        x,y,d = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0 and new_graph[nx][ny] == -1:
                q.append((nx,ny,d+1))
                new_graph[nx][ny] = d+1
    flag = True
    maxTime = -1
    for i in range(N):
        for j in range(N):
            if graph[i][j] ==0 and new_graph[i][j] == -1:
                flag = False
            maxTime = max(maxTime, new_graph[i][j])
    if flag:
        answer.append(maxTime)
    else:
        answer.append(-1)
if max(answer) == -1:
    print(-1)
else:
    minTime = 2500
    for a in answer :
        if a>0:
            minTime = min(minTime,a)
    print(minTime)