#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> convert(string s, int n)
{
    vector<string> v;
    for (int i=0; i<s.length(); i+=n) {
        //cout << s.substr(i, n) << " ";
        v.push_back(s.substr(i, n));
    }
    //cout << endl;
    return v;
}

int solution(string s){
    vector<string> tok;
    string before;
    int cnt = 1;
    int min = s.length();
    string str="";
    for (int j=1; j<=s.length()/2; j++) {
        tok = convert(s, j);
        str = "";
        before = tok[0];
        cnt = 1;
        for (int i=1; i<tok.size(); i++) {
            if(tok[i] == before) cnt++;
            else
            {
                if(cnt != 1) str += to_string(cnt);
                str += before;
                before = tok[i];
                cnt = 1;
            }
        }
        if ( cnt!=1) str += to_string(cnt);
        str += before;
        min = min < str.length() ? min : str.length();
    }

    return min;
}

int main(void){
    cout << solution("aababab") << endl;
    cout << solution("aabbaccc") << endl;
    cout << solution("ababcdcdababcdcd") << endl;
    cout << solution("abcabcdede") << endl;
    cout << solution("abcabcabcabcdededededede") << endl;
    cout << solution("xababcdcdababcdcd") << endl;
}
