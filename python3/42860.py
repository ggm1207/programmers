import heapq
from time import sleep
from string import ascii_uppercase

def cntName(n1, n2):
    return sum(map(lambda x1, x2: x1 == x2, n1, n2))

def solution(name):
    name_len = len(name)
    queue = [(name_len - cntName("A"*name_len, name), 0, 0, "A"*name_len)]
    heapq.heapify(queue)

    while True:
        weight, cnt, idx, temp = heapq.heappop(queue)
        print(temp, weight, idx)
        print("".join([(name[i]) if i == idx else " " for i in range(name_len)]))

        if temp == name: return cnt

        heapq.heappush(queue, (weight + 1, cnt + 1, (idx+1)%name_len, temp))
        heapq.heappush(queue, (weight + 1, cnt + 1, (idx-1)%name_len, temp))

        ntemp = temp[:idx] + name[idx] + temp[idx+1:]

        if temp == ntemp:
            continue

        j_cnt = min(ascii_uppercase.index(name[idx]), ascii_uppercase[::-1].index(name[idx]) + 1)

        if j_cnt:
            heapq.heappush(queue, (weight - cntName(name, ntemp), cnt + j_cnt, idx, ntemp))

        sleep(0.5)
        
 

# 안되는 케이스 있음
def best_solution(name):
    m = [ min(ord(c) - ord("A"), ord("Z") - ord(c) + 1)  for c in name  ]
    answer = 0
    where = 0
    while True:
        print(m)
        answer += m[where]
        m[where] = 0
        if sum(m) == 0:
            break
        left, right = (1, 1)
        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1
        answer += left if left < right else right
        where += -left if left < right else right
    return answer       
        
        




if __name__ == "__main__":
    t_case = []
    # t_case.append("JEROEN")
    # t_case.append("JAN")
    # t_case.append("JAAAAANA")
    # t_case.append("JAAAAANANANA")
    # t_case.append("JAZ")
    # t_case.append("AC")
    t_case.append("BBAAAA")
    t_case.append("BBBBAAAAAAAB")


    for tc in t_case:
        print(solution(tc))
        print(best_solution(tc))
