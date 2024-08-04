#include <iostream>
#include <queue>

using namespace std;
const int dx[] = {0,1,0,-1};
const int dy[] = {1,0,-1,0};
const int MAX_NUM = 20;
int graph[MAX_NUM][MAX_NUM];
int sum_graph[MAX_NUM][MAX_NUM];
bool visited[MAX_NUM][MAX_NUM];
int N,M;
int dir = 0;
int answer=0;

int numbers[][3] = {{0,1,0},{0,5,0},{4,6,3},{0,2,0}};
//  1
//  5
//4 6 3
//  2
struct Position{
    int x,y;
    Position(){};
    Position(int _x, int _y):x(_x),y(_y){};
};
Position sp = Position(0,0);

bool inRange(int x, int y){
    if (x>=0 && x<N && y>=0 && y<N) return true;
    return false;
}
void bfs(int i,int j){
    int nx,ny;
    int cnt=1;
    queue<Position> q;
    queue<Position> sum_q;
    q.push(Position(i,j));
    while (!q.empty()){
        Position p = q.front();
        q.pop();
        sum_q.push(Position(p.x,p.y));
        for (int k=0;k<4;k++){
            nx = p.x + dx[k];
            ny = p.y + dy[k];
            if(inRange(nx,ny) && !visited[nx][ny] && (graph[p.x][p.y] == graph[nx][ny])){
                visited[nx][ny] = true;
                q.push(Position(nx,ny));
                cnt+=1;
            }
        }
    }
    cnt *= graph[i][j];
    while (!sum_q.empty()){
        Position p = sum_q.front();
        sum_q.pop();
        sum_graph[p.x][p.y] = cnt;
    }
}
void calc_num(){
    
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            if (!visited[i][j]){
                visited[i][j] =true;
                bfs(i,j);
            }
        }
    }
    
}
void change_dice(int d){
    if (d==0){
        // ->
        int tmp =numbers[2][1];
        numbers[2][1] = numbers[2][2];
        numbers[2][2] = numbers[0][1];
        numbers[0][1] = numbers[2][0];
        numbers[2][0] = tmp;
    }else if (d==1){
        //아래
        int tmp =numbers[2][1];
        numbers[2][1] = numbers[3][1];
        numbers[3][1] = numbers[0][1];
        numbers[0][1] = numbers[1][1];
        numbers[1][1] = tmp;
    }else if (d==2){
        // <-
        int tmp =numbers[2][1];
        numbers[2][1] = numbers[2][0];
        numbers[2][0] = numbers[0][1];
        numbers[0][1] = numbers[2][2];
        numbers[2][2] = tmp;
    }else{
        //위
        int tmp =numbers[2][1];
        numbers[2][1] = numbers[1][1];
        numbers[1][1] = numbers[0][1];
        numbers[0][1] = numbers[3][1];
        numbers[3][1] = tmp;
    }
}
void move_dice(){
    int nx = sp.x + dx[dir];
    int ny = sp.y + dy[dir];
    if(!inRange(nx,ny)){
        dir = (dir+2)%4;
        nx = sp.x + dx[dir];
        ny = sp.y + dy[dir];
    }
    
    change_dice(dir);
    answer += sum_graph[nx][ny];
    if (numbers[2][1] > graph[nx][ny]) dir = (dir + 1)%4;
    else if (numbers[2][1] < graph[nx][ny]) dir = (dir+3)%4;
    sp.x = nx;
    sp.y = ny;
    
}
int main() {
    scanf("%d %d",&N,&M);
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            scanf("%d",&graph[i][j]);
        }
    }
    calc_num();
    
    for (int i=0;i<M;i++){
        move_dice();
    }
    printf("%d\n",answer);
    return 0;
}