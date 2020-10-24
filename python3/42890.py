from itertools import combinations

def solution(relation):
    relation_len = len(relation[0])
    tuple_len = len(relation)
    candidates = set()
    for can_len in range(1, relation_len + 1):
        for combi in combinations(range(0, relation_len), can_len):
            is_candi = set()
            for rel in relation:
                candi = "".join([rel[i]  for i  in combi])
                is_candi.add(candi)
            if len(is_candi) == tuple_len:
                for candis in candidates:
                    if set(candis).issubset(set(combi)):
                        break
                else:
                    candidates.add(combi)
    return len(candidates)


if __name__ == "__main__":
    t_case = []
    t_case.append([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

    for tc in t_case:
        print(solution(tc))
