def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    truck_in_bridge = []
    truck_weight_sum = 0
    truck_idx = 0
    cur_time = 0
    while truck_weights:
        cur_time += 1
        now_truck = truck_weights.pop()
        if truck_in_bridge:
            if truck_in_bridge[0][1] + bridge_length == cur_time:
                truck_weight_sum -= truck_in_bridge[0][0]
                truck_in_bridge = truck_in_bridge[1:]
        if truck_weight_sum + now_truck <= weight: # hi
            truck_weight_sum += now_truck
            truck_in_bridge.append((now_truck, cur_time))
        else: # bye and hi
            bye_truck_weight = 0
            for idx, (prev_truck, prev_time) in enumerate(truck_in_bridge):
                bye_truck_weight += prev_truck 
                if truck_weight_sum - bye_truck_weight + now_truck <= weight:
                    break
            prev_truck, prev_time = truck_in_bridge[idx]
            truck_in_bridge = truck_in_bridge[idx+1:]
            left_bridge = bridge_length - (cur_time - prev_time)
            truck_weight_sum += now_truck
            truck_weight_sum -= bye_truck_weight
            cur_time += left_bridge
            truck_in_bridge.append((now_truck, cur_time))
    if truck_in_bridge:
        cur_time += bridge_length
    return cur_time

if __name__ == "__main__":
    t_case = []
    t_case.append([2, 10, [7, 4, 5, 6]])
    t_case.append([3, 10, [7, 4, 5, 6]])
    t_case.append([3, 10, [5, 5, 5, 5]])
    t_case.append([100, 100, [10]])
    t_case.append([100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]])

    for tc in t_case:
        print(solution(*tc))
