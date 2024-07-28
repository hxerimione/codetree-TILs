//
//  main.cpp
//  algorithm
//
//  Created by 장혜림 on 7/28/24.
//

#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

const int dx[] = { 0,0, -1, -1, -1, 0, 1, 1, 1 };
const int dy[] = { 0,1, 1, 0, -1, -1, -1, 0, 1 };
const int MAXN = 15;
const int MAXM = 100;

int N,M;
int dir,cnt;
vector<vector<int>> graph;
vector<vector<int>> copy_graph;
//int graph[MAXN][MAXN];
bool visited[MAXN][MAXN];
vector<pair<int,int>> supplement;
queue<pair<int,int>> move_info;

bool inRange(int x,int y){
    if (x>=0 && x<N && y>=0 && y<N) return true;
    return false;
}
void move_sup(){
    int x,y,nx,ny;
    pair<int,int> mi = move_info.front();
    dir = mi.first;
    cnt = mi.second;
    move_info.pop();
    
    for (int i=0;i<supplement.size();i++){
        pair<int,int> sup = supplement[i];
        x = sup.first;
        y = sup.second;
        
        nx = x + cnt*dx[dir];
        ny = y + cnt*dy[dir];
        
        if (!inRange(nx, ny)){
            nx = (nx+N)%N;
            ny = (ny+N)%N;
        }
        supplement[i] = make_pair(nx, ny);
    }
}

void add_sup(){
    int x,y,nx,ny;
    int tmp;
    for (int i=0;i<supplement.size();i++){
        pair<int,int> sup = supplement[i];
        x = sup.first;
        y = sup.second;
        graph[x][y] ++;
    }
    for (int i=0;i<supplement.size();i++){
        pair<int,int> sup = supplement[i];
        x = sup.first;
        y = sup.second;
        tmp=0;
        for (int j=2;j<=8;j+=2){
            nx = x + dx[j];
            ny = y + dy[j];
            if (inRange(nx,ny) && graph[nx][ny] >=1)tmp++;
            
        }
        copy_graph[x][y] = graph[x][y] + tmp;
    }
    
    for (int i=0;i<supplement.size();i++){
        pair<int,int> sup = supplement[i];
        x = sup.first;
        y = sup.second;
        graph[x][y] = copy_graph[x][y];
    }
    
    
}

void change_sup(){
    int x,y;
    while(!supplement.empty()){
        pair<int,int> sup = supplement.back();
        x = sup.first;
        y = sup.second;
        supplement.pop_back();
        visited[x][y] = true;
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            if (visited[i][j])continue;
            if (graph[i][j] >=2){
                graph[i][j] -=2;
                supplement.push_back(make_pair(i,j));
            }
        }
    }
    for(int i=0; i<N; i++){
        memset(visited[i], 0, sizeof(bool)*N);
    }
}
int calc_answer(){
    int answer=0;
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            answer += graph[i][j];
        }
    }
    return answer;
}
int main() {
    // 여기에 코드를 작성해주세요.
    scanf("%d %d",&N,&M);
    graph = vector<vector<int>>(N, vector<int>(N, 0));
    copy_graph = vector<vector<int>>(N, vector<int>(N, 0));
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            scanf("%d", &graph[i][j]);
        }
    }
    
    for(int i=0;i<M;i++){
        scanf("%d %d",&dir,&cnt);
        move_info.push(make_pair(dir, cnt));
    }
    
    
    supplement.push_back(make_pair(N-2,0));
    supplement.push_back(make_pair(N-2,1));
    supplement.push_back(make_pair(N-1,0));
    supplement.push_back(make_pair(N-1,1));
    for (int i=0;i<M;i++){
        move_sup();
        
        add_sup();
        
        change_sup();
    }
    printf("%d",calc_answer());
    return 0;
}