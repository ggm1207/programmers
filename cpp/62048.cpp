#include <cstdio>
#include <iostream>

using namespace std;

int GCD(int a, int b){
    if ( a == 0 ) return b; 
    return GCD(b % a, a);
}

long long solution(int w,int h) {
    long long answer = 1;

    int gcd = GCD(w, h);
    answer = ((long)w * h) - ((long)w + h - gcd);
    return answer;
}

int main(){
    cout << solution(8, 12) << endl;
    return 0;
}
