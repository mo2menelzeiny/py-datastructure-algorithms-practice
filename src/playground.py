from queue import PriorityQueue, Queue

test_graph = {
    "A": {"B": 2, "C": 5},
    "B": {"D": 7, "C": 5},
    "C": {"D": 2, "E": 4},
    "D": {"F": 1},
    "E": {"D": 6, "F": 3},
    "F": {}
}
