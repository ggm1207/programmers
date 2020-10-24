from functools import reduce

def solution(arr):
    arr.sort()
    
    def LCM(n1, n2):
        o1, o2 = n1, n2
        while n1 != n2:
            if n1 < n2:
                n1 += o1
            else:
                n2 += o2
        return n2

    answer = reduce(LCM, arr)
    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([[2,6,8,14]]) # return 168
    t_case.append([[1,2,3]]) # return 6

    for tc in t_case:
        print(solution(*tc))
