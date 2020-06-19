import heapq


class RankTable:
    def __init__(self, k=3):
        self.max_size = k
        self.my_heap = []
        heapq.heapify(self.my_heap)

    def add(self, value, index):
        heapq.heappush(self.my_heap, HeapElement(value, index))
        if len(self.my_heap) > self.max_size:
            heapq.heappop(self.my_heap)

    def peek(self):
        return self.my_heap[0]

    def get_max_value(self):
        return self.peek().value1

    def get_all_objects(self):
        return [x.value2 for x in self.my_heap]


class HeapElement:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __lt__(self, other):
        return self.value1 > other.value1
