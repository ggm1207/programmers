import math
from datetime import datetime
from collections import defaultdict


def solution(fees, records):
    """
    - 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
    - 00:00 ~ 23:59 까지의 입/출차 내역을 바탕으로 요금을 일괄로 정산
    - 차량별 누적 주차 시간
    """
    dict_stack = defaultdict(list)
    car_time = defaultdict(lambda: datetime.strptime("00:00", "%H:%M"))

    for record in records:
        time, car, _ = record.split(" ")
        car_stack = dict_stack[car]

        if not car_stack:
            dict_stack[car].append(datetime.strptime(time, "%H:%M"))
        else:
            out_time = datetime.strptime(time, "%H:%M")
            in_time = car_stack.pop()

            dur_time = out_time - in_time
            car_time[car] += dur_time
            print(car, dur_time)

    for car, car_stack in dict_stack.items():
        if len(car_stack) == 0:
            continue

        out_time = datetime.strptime("23:59", "%H:%M")
        dur_time = out_time - car_stack[0]

        car_time[car] += dur_time

    answer = []

    for car, time in sorted(car_time.items(), key=lambda x: x[0]):
        minute = time.hour * 60 + time.minute
        up_minute = minute - fees[0]
        cost = 0

        if up_minute > 0:
            cost = math.ceil(up_minute / fees[2]) * fees[3]

        answer.append(fees[1] + cost)

    return answer


print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
