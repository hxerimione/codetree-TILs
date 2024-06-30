import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[[]]*m for _ in range(n)]
update_graph = [[[]]*m for _ in range(n)]
arr = []
answer=0
dx,dy = [0,-1,1,0,0],[0,0,0,1,-1]
for _ in range(k):
    x,y,s,d,b = map(int,input().split())
    graph[x-1][y-1]= [s,d,b]

def changeD(n):
    if n==1:
        return 2
    if n==2:
        return 1
    if n==3:
        return 4
    if n==4:
        return 3
for i in range(m):
    #1 - 열 탐색
    for j in range(n):
        if graph[j][i] != []:
            answer += graph[j][i][2]
            graph[j][i] = []
            break
    #2 - 곰팡이 이동
    for a in range(n):
        for b in range(m):
            if graph[a][b] !=[]:
                cur_s,cur_d,cur_b = graph[a][b]
                # print("cur",cur_s,cur_d,cur_b)
                #곰팡이 발견
                da = a + cur_s*dx[cur_d]
                db = b + cur_s*dy[cur_d]
                #벽과 충돌
                # print("da",da,"db",db)
                cnt=-1
                while True:
                    cnt += 1
                    if da<0 :
                        da = -da
                    elif da>=n:
                        da = 2*n-da-2
                    elif db<0:
                        db = -db
                    elif db>=m :
                        db = 2*m-db-2
                    else:
                        if cnt%2==1 :
                            cur_d = changeD(cur_d)
                        break
                # print("changed","da",da,"db",db,"cur_d",cur_d)
                #이미 곰팡이 있을 시
                if update_graph[da][db] != []:
                    # print("마주침")
                    if update_graph[da][db][2] > cur_b :
                        break
                #이동
                update_graph[da][db] = [cur_s,cur_d,cur_b]
    for a in range(n):
        for b in range(m):
            graph[a][b] = update_graph[a][b]
    update_graph = [[[]]*m for _ in range(n)]
    
    # print(graph)
    # print()
print(answer)