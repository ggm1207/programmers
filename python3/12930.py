def solution(s):
    return " ".join(
        [
            "".join([c.lower() if i % 2 else c.upper() for i, c in enumerate(word)])
            if word != ""
            else ""
            for word in s.split(" ")
        ]
    )


print(solution("try hello world"))
