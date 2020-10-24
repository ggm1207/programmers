from math import ceil

def solution(n, stations, w):
    st_idx, cur_pos = 0, 1 + w
    answer = 0

    while st_idx < len(stations):
        answer += 1
        if stations[st_idx] <= cur_pos:
            cur_pos = stations[st_idx] + w*2 + 1
            st_idx += 1
            answer -= 1
        else:
            cur_pos = cur_pos + w*2 + 1

    if n - cur_pos + w + 1 > 0:
        answer += ceil((n - cur_pos + w + 1) / (2 * w + 1))

    return answer

def w_solution(n, stations, w):
    ans = 0
    idx = 0
    location = 1

    while(location <= n) :
        if(idx < len(stations) and location >= stations[idx]-w) :
            location = stations[idx]+w+1
            idx += 1
        else :
            location += 2*w+1
            ans += 1
    return ans

if __name__ == "__main__":
    t_case = []
    t_case.append([11,[4, 11],1]) # return 3
    t_case.append([16,[9],2]) # return 3
    t_case.append([16,[],2]) # return 3
    t_case.append([16,[9],20]) # return 3
    t_case.append([16,[9],7]) # return 3
    t_case.append([200000000,[3],1]) # return 3

    for tc in t_case:
        print(solution(*tc))
        print(w_solution(*tc))
