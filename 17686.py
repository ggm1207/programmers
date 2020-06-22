import re

def solution(files):
    num_macth = re.compile("([^\d]*)([\d]*)(.*)")

    def key_fn(file):
        head, num, tail = num_macth.match(file).groups()
        return head.lower(), int(num)

    return sorted(files, key = key_fn)


if __name__ == "__main__":
    t_case = []
    t_case.append(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
    t_case.append(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])

    for tc in t_case:
        print(solution(tc))
