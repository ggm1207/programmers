from collections import defaultdict

def solution(genres, plays):
    genre_dict = defaultdict(int)
    play_dict = defaultdict(list)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre] += play
        play_dict[genre].append((idx, play)) 
    answer = []    
    for genre, _ in sorted(genre_dict.items(), key=lambda x: x[1], reverse=True):
        g_list, _ = zip(*sorted(play_dict[genre], key=lambda x: (x[1], 10e6 - x[0]))[-2:])
        answer += list(g_list[::-1])
    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]])
    
    for tc in t_case:
        print(solution(*tc))
