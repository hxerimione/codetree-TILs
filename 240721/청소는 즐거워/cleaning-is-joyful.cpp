#include <iostream>
#include <cmath>

using namespace std;
const int MAXN = 500;
int N;
int graph[MAXN][MAXN];
int answer,d,dust;
//좌 하 우 상
const int dx[] = { 0, 1, 0, -1 };
const int dy[] = { -1, 0, 1, 0 };

struct Position {
    int cur_x, cur_y;
    Position() {}
    Position(int cur_x, int cur_y) : cur_x(cur_x), cur_y(cur_y) {}
};

Position p;

bool inRange(int x,int y){
    if (x>=0 && x<N && y>=0 && y<N) return true;
    return false;
}

int dust_move(int x,int y, int ratio){
    if (inRange(x,y)){
        graph[x][y] += floor(dust*0.01*ratio);
    }else{
        answer+= floor(dust*0.01*ratio);
    }
    return floor(dust*0.01*ratio);
}

void move(int dir) {
    
    int nx,ny;
    nx = p.cur_x + dx[dir%4];
    ny = p.cur_y + dy[dir%4];
    
    dust = graph[nx][ny];
    int tmp=0;
    //1%
    tmp += dust_move(p.cur_x + dx[(dir+3)%4],p.cur_y + dy[(dir+3)%4],1);
    tmp += dust_move(p.cur_x + dx[(dir+1)%4],p.cur_y + dy[(dir+1)%4],1);

    // //2%
    tmp += dust_move(nx + 2*dx[(dir+3)%4],ny + 2*dy[(dir+3)%4],2);
    tmp += dust_move(nx + 2*dx[(dir+1)%4],ny + 2*dy[(dir+1)%4],2);

    // //5%
    tmp += dust_move(nx + 2*dx[dir%4],ny + 2*dy[dir%4],5);

    // //7%
    tmp += dust_move(nx + dx[(dir+3)%4],ny + dy[(dir+3)%4],7);
    tmp += dust_move(nx + dx[(dir+1)%4],ny + dy[(dir+1)%4],7);
    
    // //10%
    tmp += dust_move(nx + dx[dir%4] + dx[(dir+3)%4],ny + dy[dir%4] + dy[(dir+3)%4],10);
    tmp += dust_move(nx + dx[dir%4] + dx[(dir+1)%4],ny + dy[dir%4] + dy[(dir+1)%4],10);

    // //a%
    if (inRange(nx + dx[dir%4], ny + dy[dir%4])){
        graph[nx + dx[dir%4]][ny + dy[dir%4]] += dust-tmp;
    }else{
        answer+= dust-tmp;
    }
    // printf("%d %d %d\n",answer,tmp,dust);
    
    graph[p.cur_x][p.cur_y] =0;
    p.cur_x = nx;
    p.cur_y = ny;
    
}
int main() {
    scanf("%d",&N);
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            scanf("%d", &graph[i][j]);
        }
    }
    d=0;
    answer=0;
    p = Position((N-1)/2, (N-1)/2);
    for (int i=1;i<=N;i++){
        for (int j=0;j<2;j++){
            for (int k=0;k<i;k++){
                move(d);
                if (p.cur_x ==0 && p.cur_y==0){
                    printf("%d\n",answer);
                    return 0;
                }
                
            }
            d++;
        }
    }
    
}