from collections import deque

test_graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["I"],
    "D": ["G", "H"],
    "E": [],
    "F": [],
    "G": [],
    "H": ["J"],
    "I": [],
    "J": []
}


def bfs_search(graph, start, element):
    search_queue = deque()  # create a queue to preserve sequence of nodes
    search_queue += graph[start]  # add all children of each node to the queue
    checked = []  # array of checked nodes to prevent cyclic behaviour
    while search_queue:  # until the queue is empty
        current = search_queue.popleft()  # select first item
        if current == element:  # if is the element we're looking for
            return True  # return true and terminate
        elif current not in checked:  # make sure it's not checked before
            search_queue += graph[current]  # add it's children to the queue
            checked.append(current)  # add node to checked queue
    return False


print(bfs_search(test_graph, "A", "J"))
