from collections import defaultdict

def solution(n, words):
    chk_dup = defaultdict(bool)

    for idx, word in enumerate(words):
        if chk_dup[word]:
            return [(idx % n) + 1, (idx // n) + 1]
        chk_dup[word] = True 
        if idx == 0: continue

        if word[0] != words[idx-1][-1]:
            return [(idx % n) + 1, (idx // n) + 1]

    return [0, 0]

if __name__ == "__main__":
    t_case = []
    t_case.append([3, ["tank kick know wheel land dream mother robot tank".split(" ")]]) # return [33]
    t_case.append([5, ["hello observe effect take either recognize encourage ensure establish hang gather refer reference estimate executive".split(" ")]]) # return [00]
    t_case.append([2, ["hello one even never now world draw".split(" ")]]) # return [13]

    for tc in t_case:
        print(solution(*tc))
