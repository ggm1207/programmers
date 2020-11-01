#include <algorithm>
#include <vector>

using namespace std;

int gm, gn;
int dfs(int y, int x, int color, vector<vector<int>> & picture){
    if (y < 0 || y >= gm || x < 0 || x >= gn) return 0;
    if (picture[y][x] == 0 || picture[y][x] != color) return 0;
    picture[y][x] = 0;
    return 1 + dfs(y + 1, x, color, picture) + dfs(y - 1, x, color, picture) + dfs(y, x + 1, color, picture) + dfs(y, x - 1, color, picture);
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    gm = m; gn = n;
    
    for (int y=0; y<m; y++) {
        for (int x=0; x<n; x++) {
            if (picture[y][x] != 0){
                number_of_area++;
                max_size_of_one_area = max(max_size_of_one_area, dfs(y, x, picture[y][x], picture));
            }
        }
    }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;

    return answer;
}
