class Tri:
    def __init__(self, words):
        self.root = dict()

        for word in words:
            self._insert(word)

    def find(self, word):
        cnt = 0
        cur_node = self.root

        for wo in word:
            word_cnt, next_ = cur_node[wo]
            cnt += 1
            if word_cnt == 1:
                break
            else:
                cur_node = next_

        return cnt

    def _insert(self, word):
        cur_node = self.root

        for wo in word:
            cur_node[wo] = cur_node.get(wo, [0, dict()])
            cur_node[wo][0] = cur_node[wo][0] + 1
            cur_node = cur_node[wo][1]


def solution(words):
    answer = 0
    tri = Tri(words)

    for word in words:
        answer += tri.find(word)

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append(["go,gone,guild".split(",")])  # return 7
    t_case.append(["abc,def,ghi,jklm".split(",")])  # return 4
    t_case.append(["word,war,warrior,world".split(",")])  # return 15

    for tc in t_case:
        print(solution(*tc))
