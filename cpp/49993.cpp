#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

bool check_skill_tree(string &skill, string &skill_tree)
{
    cout << skill << " " << skill_tree << endl;
    
    map<char, int> m;
    
    int seq = 1;

    for (int i=0; i < skill_tree.size(); i++) {
        auto it = find(skill.begin(), skill.end(), skill_tree[i]);
        if (it != skill.end())
            m.insert(make_pair(skill_tree[i], seq++));
    }

    for (auto it=m.begin(); it != m.end(); it++) {
        cout << "key: " << it -> first << " " << "value: " << it -> second << endl;
    }

    bool flag = true;
    seq = 1;
    int temp;

    for (int i=0; i < skill.size(); i++) {
        cout << m.find(skill[i]) -> first << " " ;
        cout << m.find(skill[i]) -> second << endl;
        temp = m.find(skill[i]) -> second;
        if (temp==0){
            seq++;
            continue;
        }

        if(temp != seq++){
            flag = false;
            break;
        }
    }

    
    return flag;
}

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;

    for (int i=0; i < skill_trees.size(); i++) {
        if (check_skill_tree(skill, skill_trees[i]))
            answer++;
    }

    return answer;
}


int main(){
    string skill = "CBD";
    vector<string> skill_trees = {"BACDE", "CBADF", "AECB", "BDA"};
    cout << solution(skill, skill_trees) << endl;
}
