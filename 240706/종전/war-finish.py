N =int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
dx,dy = [0,-1,-1,1,1],[0,1,-1,-1,1]
total = 0
for i in range(N):
    for j in range(N):
        total += graph[i][j]
answer=[]
def calculate(a,b,odd,even):
    new_graph = [[0] * (N) for _ in range(N)]
    new_graph[a][b] = 1
    for i in range(1,odd+1):
        #왼쪽 아래로 - line3
        new_graph[a+i][b-i] = 1
    for i in range(1,even+1):
        #오른쪽 아래로 - line4
        new_graph[a+odd+i][b-odd+i] = 1
    for i in range(1,odd+1):
        #오른쪽 위로 - line 1
        new_graph[a+odd+even-i][b-odd+even+i] = 1
    for i in range(1,even+1):
        #왼쪽 위로 == (a,b)에서 오른쪽 아래로 - line2
        new_graph[a+i][b+i] = 1

    area = [0]*5
    #1번 지역 (왼쪽 위)
    for ii in range(a+odd): #0<=x<a+odd
        for jj in range(b+1): #0<y<=b
            if new_graph[ii][jj] == 1:
                break
            area[1] += graph[ii][jj]
    #2번 지역 (오른쪽 위) 
    for ii in range(a+even+1):#0<=x<=a+even
        for jj in range(N-1,b,-1): #b<y<N
            if new_graph[ii][jj] == 1:
                break
            area[2] += graph[ii][jj]
    #3번 지역 (왼쪽 아래)
    for ii in range(N-1,a+odd-1,-1): # a+odd<=x<N
        for jj in range(b-odd+even):# 0<=y<b-odd+even
            if new_graph[ii][jj] == 1:
                break
            area[3] += graph[ii][jj]
    #4번 지역 (오른쪽 아래)
    for ii in range(N-1,a+even,-1):#a+even<x<N
        for jj in range(N-1,b-odd+even-1,-1): #b-odd+even<=y<N
            if new_graph[ii][jj] == 1:
                break
            area[4] += graph[ii][jj]
    #5번 지역 (직사각형 안)

    area[0] = total - sum(area)

    return max(area)-min(area)


for i in range(N):
    for j in range(N):
        for odd in range(1,N+1):
            for even in range(1,N+1):
                # (i,j)는 직사각형의 가장 윗 점
                if i + odd + even >= N :
                    continue
                if j - odd < 0 :
                    continue
                if j + even >= N :
                    continue
                answer.append(calculate(i,j,odd,even))

print(min(answer))