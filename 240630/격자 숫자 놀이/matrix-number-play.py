import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
A = []
for _ in range(3):
    A.append(list(map(int,input().split())))
time =0
from collections import defaultdict
import heapq
q=[]
while True:
    time += 1
    #100이상
    if len(A)>100 or len(A[0])>100 :
        graph=[]
        for i in range(min(100,len(A))):
            for j in range(min(100,len(A[0]))):
                graph[i][j]=A[i][j]
        for i in range(graph):
            for j in range(graph[0]):
                A = graph[i][j]
    
    #행 기준
    if len(A) >= len(A[0]):
        for i in range(len(A)):
            dic = defaultdict(int)
            for j in range(len(A[i])):
                dic[A[i][j]]+=1

            for k,v in dic.items() :
                if k>0:
                    heapq.heappush(q,(v,k))
            
            A[i]=[]

            while q:
                v,k = heapq.heappop(q)
                A[i].append(k)
                A[i].append(v)
        m=0
        for i in range(len(A)):
            m = max(m,len(A[i]))
        for i in range(len(A)):
            if m>len(A[i]):
                for _ in range(m-len(A[i])):
                    A[i].append(0)
    #열 기준
    else:
        for j in range(len(A[0])):
            dic = defaultdict(int)
            for i in range(len(A)):
                dic[A[i][j]]+=1
            for k,v in dic.items() :
                if k>0:
                    heapq.heappush(q,(v,k))

            
            #열 추가하기
            idx=0
            while q:
                v,k = heapq.heappop(q)
                if len(A)<=idx:
                    A.append([0]*len(A[0]))
                A[idx][j] = k
                idx+=1
                if len(A)<=idx:
                    A.append([0]*len(A[0]))
                A[idx][j] = v
                idx+=1

        # m=len(A)
        # for i in range(len(A)):
            
        #     if m>len(A[i]):
        #         for _ in range(m-len(A[i])):
        #             A[i].append(0)


    if len(A)>=r and len(A[r-1])>=c and A[r-1][c-1] == k :
        print(time)
        break
    if time>100:
        print(-1)
        break