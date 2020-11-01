#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

class PQueue{
    private:
        vector<int> answer;
        int length=0;
        int bottom=0;
    public:
        void insert(int item);
        int delete_max();
        int delete_min();
        bool is_empty();
};

bool PQueue::is_empty(){
    return answer.size() == 0;
}

void PQueue::insert(int item){
    int mid = -1; 

    for (int i=0; i<answer.size(); i++) {
        if(item > answer[i]) continue;
        else mid = i;
    }
    
    if(mid == -1)
        answer.push_back(item);
    else
        answer.insert(answer.begin() + mid, item);

    //for (int i=0; i<answer.size(); i++) {
        //cout << answer[i] << " ";
    //}
    //cout << endl;
}

int PQueue::delete_max(){
    if(is_empty()) return 0; // ignore
    int item = answer.back();
    answer.erase(answer.end() - 1);
    return item;
}

int PQueue::delete_min(){
    if(is_empty()) return 0;
    int item = answer.front();
    answer.erase(answer.begin());
    return item;
}

vector<string> split(string str, char delimiter){
    vector<string> internal;
    stringstream ss(str);
    string temp;
    
    while(getline(ss, temp, delimiter)){
        internal.push_back(temp);
    }
    return internal;
}


vector<int> solution(vector<string> operations) {
    vector<int> answer;
    vector<string> temp;
    int item;

    PQueue pq = PQueue();

    for (auto it: operations){
        temp = split(it, ' ');
        item = stoi(temp[1]);
        if(temp[0] == "I") pq.insert(item);
        else if(temp[1] == "1") pq.delete_max();
        else pq.delete_min();
    }
    
    if (pq.is_empty()){
        answer.push_back(0);
        answer.push_back(0);
    } else {
        answer.push_back(pq.delete_max());
        answer.push_back(pq.delete_min());
    }
    
    //for (auto it: answer){
        //cout << it << " ";
    //}
    //cout << endl;

    return answer;
}

int main(void){
    //solution({"I 16", "D 1"});
    //solution({"I 7", "I 5", "I -5", "D -1"});
    solution({"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"});
    return 0;
}
