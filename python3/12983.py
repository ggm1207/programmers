from collections import defaultdict

def solution(strs, t):
    t_vocab = defaultdict(list)
    max_len = len(t) + 1
    answer = [max_len] * len(t)
    
    for vocab in strs:
        t_vocab[vocab[-1]].append(vocab)

    for i in range(len(t)):
        vocabs = t_vocab[t[i]]

        if not vocabs:
            answer[i] = max_len
            continue

        # find_subword
        for vocab in vocabs:
            compare_vocab = t[i-len(vocab)+1:i+1]
            if vocab == compare_vocab:
                if i - len(vocab) >= 0:
                    answer[i] = min(answer[i-len(vocab)] + 1, answer[i])
                else:
                    answer[i] = 1
                
    return -1 if answer[-1] == max_len else answer[-1]



if __name__ == "__main__":
    t_case = []
    t_case.append([["ba,na,n,a".split(",")][0], "banana"])  # return 3
    t_case.append([["app,ap,p,l,e,ple,pp".split(",")][0], "apple"])  # return 2
    t_case.append([["ba,an,nan,ban,n".split(",")][0], "banana"])  # return -1
    # t_case.append([["ba,na,n,a".split(",")][0], "banana" * 100])
    # t_case.append([["ba,an,nan,ban,n".split(",")][0], "banana" * 100])

    for tc in t_case:
        print(solution(*tc))
