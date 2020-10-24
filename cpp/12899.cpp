#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(int n){
    string answer = "";
    int a;
    while ( n > 0 ){
        a = n % 3;
        n = n / 3;
        if ( a == 0 ){
            n -= 1;
        }
        answer = "412"[a] + answer;
    }

    return answer;
}


int main(void){
    cout << solution(1) << endl;
    cout << solution(2) << endl;
    cout << solution(3) << endl;
    cout << solution(4) << endl;
    cout << solution(5) << endl;
    return 0;
}
