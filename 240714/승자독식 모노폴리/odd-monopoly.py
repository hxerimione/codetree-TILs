import sys
from collections import deque,defaultdict
input = sys.stdin.readline
dx,dy = [0,-1,1,0,0],[0,0,0,-1,1]
n,m,k = map(int,input().split())

graph = [[] for _ in range(n)] #계약
move_graph = [[] for _ in range(n)] #위치

for i in range(n):
    arr = list(map(int,input().split()))
    for a in arr:
        move_graph[i].append([a])
        if a==0:
            graph[i].append([0,0])
        else:
            graph[i].append([a,k])
#플레이어 방향
direction = [0] + list(map(int,input().split()))

live = [0] + [1]*m

#방향 우선순위
priority_d = defaultdict(list)
for i in range(1,m+1):
    priority_d[i].append([0])
    for _ in range(4):
        priority_d[i].append(list(map(int,input().split())))

for T in range(1,1000):
    #이동
    for i in range(n):
        for j in range(n):
            if move_graph[i][j][0] >0:
                p = move_graph[i][j][0]
                d_now = direction[p]
            else:
                continue
            next_x,next_y,next_d= -1,-1,-1
            for d in priority_d[p][d_now]:
                #아무도 독점계약 안한 칸 찾기
                nx = i+ dx[d]
                ny = j+ dy[d]
                if 0<=nx<n and 0<=ny<n and graph[nx][ny][0] ==0 :
                    next_x,next_y,next_d = nx,ny,d
                    break
            else:
                #내가 독점계약 한 찾기
                for d in priority_d[p][d_now]:
                    nx = i+ dx[d]
                    ny = j+ dy[d]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny][0] ==p :
                        next_x,next_y,next_d = nx,ny,d
                        break
            # 이동
            move_graph[next_x][next_y].append(p)
            move_graph[i][j] = [0]
            # 방향 갱신
            direction[p] = next_d
            
    #겹치는 경우 제일 작은 플레이어만 남기기
    for i in range(n):
        for j in range(n):
            if len(move_graph[i][j])>1:
                if 0 in move_graph[i][j]:
                    move_graph[i][j].remove(0)
                min_p = min(move_graph[i][j])
                for pi in move_graph[i][j] :
                    if pi != min_p:
                        live[pi] = 0
                move_graph[i][j] = [min_p]
                
    #독점 계약기간 줄이기
    for i in range(n):
        for j in range(n):
            if graph[i][j][1] >1:
                graph[i][j][1]-=1
            elif graph[i][j][1] ==1:
                graph[i][j] = [0,0]
    # 새 계약
    for i in range(n):
        for j in range(n):
            if move_graph[i][j][0]>0:
                if graph[i][j][0] ==0 :
                    graph[i][j] = [move_graph[i][j][0],k]
                elif graph[i][j][0] == move_graph[i][j][0] :
                    graph[i][j][1] =k
    if sum(live) == 1:
        print(T)
        break
    # print("T",T)
    # print("g",graph)
    # print("move",move_graph)
else:
    print(-1)