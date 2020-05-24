def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=lambda x: len(x))
    for l_idx in range(len(phone_book)-1):
        for r_idx in range(l_idx + 1, len(phone_book)):
            if phone_book[r_idx].startswith(phone_book[l_idx]):
                answer = False
                break
    return answer


# Consider Efficiency
class Tri(object):
    def __init__(self):
        self.root = dict()

    def insert(self, s):
        self.cur = self.root
        s_len = len(s)
        c_len = 0
        while(s_len != c_len):
            self.cur[s[c_len]] = self.cur.get(s[c_len], dict())
            if self.cur.get('end', False):
                return False
            self.cur = self.cur.get(s[c_len])
            c_len += 1
        self.cur['end'] = True
        if len(self.cur.keys()) != 1:
            return False
        return True


def solution(phone_book):
    a = Tri()
    for phone in phone_book:
        if not a.insert(phone):
            return False
    return True


if __name__ == "__main__":
    t_case = []
    t_case.append(["119", "97674223", "1195524421"])
    t_case.append(["123", "456", "789"])
    t_case.append(["12", "123", "1235", "567", "88"])

    for tc in t_case:
        print(solution(tc))
