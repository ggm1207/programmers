""" 
    - 레벨 1인데 왜 구현문제 같지...
    - 다른 사람 풀이 봐야겠다..
        - replace 많이 썻네.
"""


def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    twice_words = [word + word for word in words]

    babbling_with_no_twice_words = []

    for babble in babbling:

        flag = True

        for twice_word in twice_words:
            if twice_word in babble:
                flag = False
                break

        if flag:
            babbling_with_no_twice_words.append(babble)

    for babble in babbling_with_no_twice_words:
        s_idx = 0

        while s_idx < len(babble):
            flag = False
            for word in words:
                if word == babble[s_idx : s_idx + len(word)]:
                    s_idx += len(word)
                    flag = True
                    break

            if not flag:
                break

        if s_idx == len(babble):
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
