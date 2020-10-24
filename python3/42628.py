class Heap:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        idx = 0
        while idx < len(self.queue):
            if value <= self.queue[idx]:
                break
            idx += 1
        self.queue.insert(idx, value)
    
    def delete_max(self):
        self.queue = self.queue[:-1]

    def delete_min(self):
        self.queue = self.queue[1:]

    def get_solution(self):
        if self.queue:
            return [max(self.queue), min(self.queue)]
        else:
            return [0, 0]

def solution(operations):
    heap = Heap()
    for ops in operations:
        op, value = ops.split(" ")
        if op == "I":
            heap.insert(int(value))
        elif op == "D" and value == "1":
            heap.delete_max()
        else:
            heap.delete_min()
    return heap.get_solution()


if __name__ == "__main__":
    t_case = []
    t_case.append(["I 16", "D 1"])
    t_case.append(["I 7", "I 5", "I -5", "D -1"])

    for tc in t_case:
        print(solution(tc))
