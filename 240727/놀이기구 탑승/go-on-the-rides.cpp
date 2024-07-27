#include <iostream>
using namespace std;

const int MAXN=20;
const int dx[] = { 0, 1, 0, -1 };
const int dy[] = { -1, 0, 1, 0 };

int N,M;
int friends[MAXN*MAXN+1][4];
int graph[MAXN][MAXN];
int order[MAXN*MAXN];

struct Block{
    int like,blank,r,c;
    Block(int r, int c) : r(r), c(c), like(-1), blank(-1) {}
};

bool inRange(int x,int y){
    if (x>=0 && x<N && y>=0 && y<N) return true;
    return false;
}

void fill(int num) {
    Block b = Block(0,0);
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            if(graph[i][j] !=0)continue;
            int like_cnt=0;
            int blank_cnt =0;
            for (int k=0;k<4;k++){
                int nx = i + dx[k];
                int ny = j + dy[k];
                if (inRange(nx,ny)){
                    if (graph[nx][ny] ==0){
                        blank_cnt ++;
                        continue;
                    }
                    for (int l=0;l<4;l++){
                        if (friends[num][l] == graph[nx][ny]){
                            
                            like_cnt ++;
                            break;
                        }
                    }
                }
            }
            
            if (like_cnt > b.like){
                b.r = i;
                b.c = j;
                b.blank = blank_cnt;
                b.like = like_cnt;
            }else if (like_cnt == b.like && blank_cnt > b.blank){
                b.r = i;
                b.c = j;
                b.blank = blank_cnt;
                b.like = like_cnt;
            }
            
        }
        
    }
    graph[b.r][b.c] = num;
}
int calc(int x,int y){
    int num = graph[x][y];
    int f=0;
    for (int k=0;k<4;k++){
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (inRange(nx,ny)){
            for(int i=0;i<4;i++){
                if(graph[nx][ny] == friends[num][i]){
                    f++;
                }
            }
        }
    }
    switch(f){
        case 0:
            return 0;
            break;
        case 1:
            return 1;
            break;
        case 2:
            return 10;
            break;
        case 3:
            return 100;
            break;
        case 4:
            return 1000;
            break;
        default:
            break;
    }
}
int main() {
    // 여기에 코드를 작성해주세요.
    int answer=0;
    scanf("%d",&N);
    for (int i =0;i<N*N;i++){
        cin >> M;
        cin >>friends[M][0] >> friends[M][1] >> friends[M][2] >> friends[M][3];
        // scanf("%d %d %d %d %d",&M,&friends[M][0],&friends[M][1],&friends[M][2],&friends[M][3]);
        order[i] = M;
    }
    // for (int i=0;i<=N*N;i++){
    //     printf("%d %d %d %d\n",friends[i][0],friends[i][1],friends[i][2],friends[i][3]);
    // }
    // printf("\n");
    for (int i=0;i<N*N;i++){
        fill(order[i]);
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            answer += calc(i,j);
        }
    }
    // for (int i=0;i<3;i++){
    // printf("%d %d %d\n",graph[i][0],graph[i][1],graph[i][2]);
    // }
    printf("%d",answer);
    return 0;
}