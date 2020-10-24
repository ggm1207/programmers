from collections import defaultdict

class ROOM:
    __slots__ = ("info", "prev")
    def __init__(self, num):
        self.info = {"room_number": num}
        self.prev = set()
# Linked List 로 접근해서 풀려고 했으나 잘 작동하지 않음.
def solution(k, room_number):
    answer = []
    hotel_rooms = {rn: ROOM(rn) for rn in set(room_number)}
    room_number_len = len(room_number)

    for wanted_room_number in room_number:
        real_room_number = hotel_rooms[wanted_room_number].info["room_number"]
        real_next_number = real_room_number + 1

        if real_next_number in hotel_rooms:
            hotel_rooms[wanted_room_number].info = hotel_rooms[real_next_number].info

            if hotel_rooms[wanted_room_number].prev:
                for prev_hotels in hotel_rooms[wanted_room_number].prev:
                    prev_hotels.info = hotel_rooms[real_next_number].info

            hotel_rooms[real_next_number].prev.add(hotel_rooms[wanted_room_number])
        else:
            hotel_rooms[wanted_room_number].info["room_number"] += 1

        answer.append(real_room_number)

    return answer

m = defaultdict(int)

def find(key):
    if not m[key]:
        return key
    m[key] = find(m[key])
    return m[key]

def other_solution(k, room_number):
    answer = []

    for cur in room_number:
        if not m[cur]:
            answer.append(cur)
            m[cur] = find(cur + 1)
        else:
            tmp = find(cur)
            answer.append(tmp)
            m[tmp] = find(tmp + 1)
    return answer
    
    


if __name__ == "__main__":
    t_case = []
    # t_case.append([10,[1,3,4,1,3,1,4]]) # return [1,3,4,2,5,6]
    # t_case.append([10,[6,5,4,3,2,2,2,2,1]])
    # t_case.append([10,[1,3,4,3,3,2,1]])
    # t_case.append([1000,[1,3,4,3,3,2,1,3,3,10,23,22]])
    # t_case.append([1000,[10,9,8,7,6,5,4,3,2,1,11,11,12,15,20,16,16,16,16,16]])
    # t_case.append([10,[6, 5, 4, 4, 5, 3, 2, 2]]) # return [1,3,4,2,5,6]
    # t_case.append([100,[i + 1 for i in range(100)]]) # return [1,3,4,2,5,6]
    # t_case.append([100,[1 for i in range(20)]]) # return [1,3,4,2,5,6]
    t_case.append([100,[1, 1]]) # return [1,3,4,2,5,6]

    for tc in t_case:
        print(other_solution(*tc))
