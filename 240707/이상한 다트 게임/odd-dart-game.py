import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())
circle = []
dx, dy = [-1,0,1,0],[0,-1,0,1]
for _ in range(n):
    circle.append(list(map(int,input().split())))

def rotate(idx,d,k):
    tmp=[]
    for i in range(m):
        tmp.append(circle[idx][i])
    if d==0:
        #시계
        for i in range(m):
            circle[idx][i] = tmp[i-k]
    else:
        #반시계
        for i in range(m):
            circle[idx][i] = tmp[(i+k)%m]

    
for _ in range(q):
    x,d,k = map(int,input().split())
    while x<=n:
        #x-1번째 배열 회전
        rotate(x-1,d,k)
        x += x
    check_graph = [[0]*m for _ in range(n)]
    #인접
    flag = True
    for i in range(n):
        for j in range(m-1):
            for r in range(4):
                ni = i + dx[r]
                nj = j + dy[r]
                if 0<=ni<n and circle[i][j] == circle[ni][nj] :
                    check_graph[i][j] = 1
                    check_graph[ni][nj] = 1
                    flag = False
    
    if flag:
        total = 0 
        count = 0
        #인접 없을 때 -> 정규화
        for i in range(n):
            for j in range(m):
                if circle[i][j] >0:
                    total += circle[i][j]
                    count += 1
        average = total//count
        for i in range(n):
            for j in range(m):
                if circle[i][j] >0:
                    if circle[i][j] > average:
                        circle[i][j] -=1
                    elif circle[i][j] < average:
                        circle[i][j] +=1
    else:
        #인접하면 -> 삭제
        for i in range(n):
            for j in range(m):
                if check_graph[i][j] ==1 :
                    circle[i][j] = 0

answer =0
for i in range(n):
    answer += sum(circle[i])
print(answer)