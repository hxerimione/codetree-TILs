# import sys
# input = sys.stdin.readline
# dx,dy = [0,-1,-1,0,1,1,1,0,-1],[0,0,-1,-1,-1,0,1,1,1]
# horse = []
# answer=0
# graph=[[0]*4 for _ in range(4)]
# for i in range(4):
#     arr = list(map(int,input().split()))
#     for j in range(4):
#         graph[i][j] = [arr[2*j],arr[2*j+1]]

# def move():
#     location = [0]* 17
#     for i in range(4):
#         for j in range(4):
#             if graph[i][j][0] >0:
#                 location[graph[i][j][0]] = [i,j]
#     for k in range(1,17,1): 
#         if location[k] != 0 :
#             i,j = location[k]
#             d = graph[i][j][1]
#             while True :
#                 ni = i + dx[d]
#                 nj = j + dy[d]
#                 if 0<=ni<4 and 0<=nj<4:        
#                     if graph[ni][nj] == [-1,-1]:
#                         #술래
#                         d = (d+1)%8
#                         if d==0:
#                             d = 8
#                     else:
#                         #빈칸 or 다른 도둑말
#                         tmp = graph[ni][nj][0]
#                         graph[i][j],graph[ni][nj] = graph[ni][nj],graph[i][j]
#                         location[k],location[tmp] = location[tmp],location[k]
#                         break           
#                 else:
#                     d = (d+1)%8 
#                     if d==0:
#                         d = 8
#                 if d == graph[i][j][1]:
#                     break
#     print(graph)

# def DFS(x,y,d,num):
#     global answer
#     num += graph[x][y][0]
#     print(num)
#     graph[x][y] = [-1,-1]
#     # 이동
#     move()
#     # 먹을 수 있는 것
#     for k in range(1,4,1):
#         nx = x + k * dx[d]
#         ny = y + k * dy[d]
#         if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0]!=0 :
#             graph[x][y] = [0,0]
#             DFS(nx,ny,graph[nx][ny][1],num)
#             graph[x][y] = [-1,-1]
#         else:
#             print(answer,num)
#             answer = max(answer,num)

# num, direct = graph[0][0]
# DFS(0,0,direct,0)
# # graph[0][0] = [-1,-1]
# # move()
# # 술래 : [-1,-1]
# # 빈칸 : [0,0]
# print(answer)



import sys
input = sys.stdin.readline
import copy
dx,dy = [0,-1,-1,0,1,1,1,0,-1],[0,0,-1,-1,-1,0,1,1,1]
horse = []
answer=0
horse=[[0]*4 for _ in range(4)]
for i in range(4):
    arr = list(map(int,input().split()))
    for j in range(4):
        horse[i][j] = [arr[2*j],arr[2*j+1]]

def move(graph):

    location = [0]* 17
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] >0:
                location[graph[i][j][0]] = [i,j]
    for k in range(1,17,1): 
        if location[k] != 0 :
            i,j = location[k]
            d = graph[i][j][1]
            while True :
                ni = i + dx[d]
                nj = j + dy[d]
                if 0<=ni<4 and 0<=nj<4:        
                    if graph[ni][nj] == [-1,-1]:
                        #술래
                        d = (d+1)%8
                        if d==0:
                            d = 8
                    else:
                        #빈칸 or 다른 도둑말
                        tmp = graph[ni][nj]
                        graph[ni][nj] = [graph[i][j][0],d]
                        graph[i][j] = tmp
                        
                        # graph[i][j],graph[ni][nj] = graph[ni][nj],graph[i][j]
                        location[k],location[tmp[0]] = location[tmp[0]],location[k]
                        break           
                else:
                    d = (d+1)%8 
                    if d==0:
                        d = 8
                if d == graph[i][j][1]:
                    break
    return graph

def DFS(x,y,d,num,graph):
    global answer
    num += graph[x][y][0]

    graph[x][y] = [-1,-1]
    # 이동
    graph = move(graph)
    # 먹을 수 있는 것
    for k in range(1,4,1):
        nx = x + k * dx[d]
        ny = y + k * dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0]!=0 :
            graph[x][y] = [0,0]
            DFS(nx,ny,graph[nx][ny][1],num,copy.deepcopy(graph))
            graph[x][y] = [-1,-1]
        else:

            answer = max(answer,num)

num, direct = horse[0][0]
DFS(0,0,direct,0,horse)
print(answer)