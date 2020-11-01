#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n){
    vector<int> answer;
    int max_n, y, x, my, mx, cnt, dir;
    int arr[1000][1000] = { 0 };
    int direction[3][2] = {{1, 0}, {0, 1}, {-1, -1}};  // (y, x)

    max_n = (n + 1) * n / 2;
    y=0; x=0; cnt=1; dir=0;

    while(cnt < max_n + 1){
        arr[y][x] = cnt;

        my = y + direction[dir][0];
        mx = x + direction[dir][1];

        if((my == (n-1) && mx == 0) || mx == (n-1) || arr[my][mx] != 0)
            dir = (dir + 1) % 3;

        if(arr[my][mx] != 0){
            my = y + direction[dir][0];
            mx = x + direction[dir][1];
        }

        y = my; x = mx;
        
        cnt++;

    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<i+1; j++) {
            answer.push_back(arr[i][j]);
        }
    }
    
    return answer;
}

int main(void){

    int arr[10][10] = { 0 };
    
    //for (int i=0; i<10; i++) {
        //for (int j=0; j<10; j++) {
            //cout << arr[i][j] << " ";
        //}
        //cout << endl;
    //}

    solution(4);
    solution(5);
    solution(6);
    return 0;
}
