def solution(arr1, arr2):
    temp = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                temp[i][j] += arr1[i][k] * arr2[k][j]
    return temp

def best_solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1]

if __name__ == "__main__":
    t_case = []
    t_case.append([[[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]]) # return [[15, 15], [15, 15], [15, 15]]
    t_case.append([[[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]]) # return [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

    for tc in t_case:
        print(solution(*tc))
        print(best_solution(*tc))
