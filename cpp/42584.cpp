#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    int cost;

    for (int i=0; i < (prices.size() - 1); i++) {
        cost = 0;
        for (int j = (i + 1); j < prices.size(); j++) {
            if (prices[i] <= prices[j])
                cost++;
            else {
                cost++;
                break;
            }
        }
        answer.push_back(cost);
    }
    
    answer.push_back(0);

    return answer;
}

int main(){
    vector<int> testcase = {1, 2, 3, 2, 3};
    solution(testcase);

    //cout << solution(testcase) << endl;
        
    return 0;
}
