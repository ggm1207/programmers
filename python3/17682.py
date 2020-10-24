import re

def solution(dartResult):
    answer = []

    for dart in re.findall("\d*.", dartResult):
        if dart in ["*", "#"]:
            if dart == "*":
                answer[-2:] = list(map(lambda x: x * 2, answer[-2:]))
            else:
                answer[-1] = answer[-1] * (-1)
            continue

        answer.append(pow(int(dart[:-1]), ["F","S","D","T"].index(dart[-1])))

    return sum(answer)

if __name__ == "__main__":
    t_case = []
    t_case.append("1S2D*3T")  # 37
    t_case.append("1D2S#10S")  # 9
    t_case.append("1D2S0T")  # 3
    t_case.append("1S*2T*3S")  # 23
    t_case.append("1D#2S*3S")  # 5
    t_case.append("1T2D3D#")  # -4
    t_case.append("1D2S3T*")  # 59

    for tc in t_case:
        print(solution(tc))
