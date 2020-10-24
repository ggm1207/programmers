def solution(participant, completion):
    p, c = sorted(participant), sorted(completion) 
    p_idx, c_idx = 0, 0
    try:
        while(p[p_idx] == c[c_idx]):
            p_idx += 1
            c_idx += 1
    except:
        pass
    answer = p[p_idx]
    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([["leo","kiki","eden"],["eden","kiki"]])
    t_case.append([["marina","josipa","nikola","vinko","filipa"],["josipa","filipa","marina","nikola"]])
    t_case.append([["mislav","stanko","mislav","ana"],["stanko","ana","mislav"]])

    for tc in t_case:
        print(solution(*tc))    
