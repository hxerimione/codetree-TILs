import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
color = []
dx,dy = [0,0,0,-1,1],[0,1,-1,0,0]
for _ in range(n):
    color.append(list(map(int,input().split())))
graph=[[""]*n for _ in range(n)]
horse=[]
for idx in range(k):
    x,y,d = map(int,input().split())
    graph[x-1][y-1] += str(idx)
    # graph[x-1][y-1].append((idx,d))
    horse.append([x-1,y-1,d])
def change(d):
    if d==1:
        return 2
    if d==2:
        return 1
    if d==3:
        return 4
    if d==4:
        return 3
def move_white(i,x,y,nx,ny,d):
    for j in range(len(graph[x][y])):
        if graph[x][y][j] == str(i):
            for movehorse in graph[x][y][j:]:
                horse[int(movehorse)][0] = nx
                horse[int(movehorse)][1] = ny
            graph[nx][ny] += graph[x][y][j:]
            # horse[i] = [nx,ny,d]
            graph[x][y] = graph[x][y][:j]
            if len(graph[nx][ny])>=4:
                return False
            else:
                return True

def move_red(i,x,y,nx,ny,d):
    for j in range(len(graph[x][y])):
        if graph[x][y][j] == str(i):
            for movehorse in graph[x][y][j:]:
                horse[int(movehorse)][0] = nx
                horse[int(movehorse)][1] = ny
            graph[nx][ny] += graph[x][y][j:][::-1]
            # horse[i] = [nx,ny,d]
            graph[x][y] = graph[x][y][:j]
            if len(graph[nx][ny])>=4:
                return False
            else:
                return True

def move_blue(i,x,y,nx,ny,d):
    nx = x+dx[d]
    ny = y+dy[d]
    if (nx<0 or nx>=n or ny<0 or ny>=n) or color[nx][ny] ==2:
        #범위 벗어나거나 파란색일 경우
        horse[i][2] = change(d)
        nnx = x+dx[horse[i][2]]
        nny = y+dy[horse[i][2]]
        if (nnx<0 or nnx>=n or nny<0 or nny>=n) or color[nnx][nny] ==2:
            return True
        elif color[nnx][nny] ==0:
        #흰색
            return move_white(i,x,y,nnx,nny,d)
        elif color[nnx][nny] ==1:
        #빨간색
            return move_red(i,x,y,nnx,nny,d)
        
flag = True

for T in range(1,1001):
    for i in range(k):
        x,y,d = horse[i]
        nx = x+dx[d]
        ny = y+dy[d]
        if (nx<0 or nx>=n or ny<0 or ny>=n) or color[nx][ny] ==2:
        #범위 벗어나거나 파란색일 경우
            flag = move_blue(i,x,y,nx,ny,d)
        elif color[nx][ny] ==0:
        #흰색
            flag = move_white(i,x,y,nx,ny,d)
        elif color[nx][ny] ==1:
        #빨간색
            flag = move_red(i,x,y,nx,ny,d)
        if not flag:
            print(T)
            exit(0)
if flag:
    print(-1)

# 답이 1000보다 크거나 불가능한 경우에는 -1을 출력