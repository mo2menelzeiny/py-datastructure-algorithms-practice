from collections import deque
from queue import PriorityQueue

# hash map representation of a graph problem
test_graph = {
    "A": {"B": 2, "C": 5},
    "B": {"D": 7, "C": 5},
    "C": {"D": 2, "E": 4},
    "D": {"F": 1},
    "E": {"D": 6, "F": 3},
    "F": {}
}

costs = {
    "A": 0,
    "B": float("inf"),
    "C": float("inf"),
    "D": float("inf"),
    "E": float("inf"),
    "F": float("inf")
}

parents = {
    "A": None,
    "B": None,
    "C": None,
    "D": None,
    "E": None,
    "F": None
}

processed = []


def dijkstra(g: dict, c: dict, pa: dict, pr: list, start, end):
    current_key = start  # set current key as start key
    while current_key is not end:  # loop while current node key is not last node
        for child_key in g[current_key].keys():  # loop on current parent neighbours
            path_cost = c[current_key] + g[current_key][child_key]  # parent weight + edge
            if c[child_key] > path_cost and child_key not in pr:  # if path cost > current cost of node update
                c[child_key] = path_cost  # update cost of selected neighbour
                pa[child_key] = current_key  # update parent
        pr.append(current_key)  # mark node as processed
        # Find cheapest next not processed node key by using min element algorithm
        cheapest_weight = float("inf")
        cheapest_key = None
        for node_key in c.keys():
            if c[node_key] < cheapest_weight and node_key not in pr:
                cheapest_weight = c[node_key]
                cheapest_key = node_key
        current_key = cheapest_key
    return pa, c[end]


def dijkstra_pq(g: dict, source, target):
    # initialize
    dist: dict = {source: 0}
    prev = {}
    pq = PriorityQueue()
    pq.put((0, source))
    # populate distance list
    for node_key in test_graph.keys():
        if node_key != source:
            dist[node_key] = float('inf')
    # while queue is not empty
    while pq.queue:
        node_dist, node_key = pq.get()  # priority pop least distance node
        neighbours = test_graph[node_key]  # get neighbour nodes
        if node_dist > dist[node_key]:  # if distance of node popped greater that that saved reset loop
            continue
        for neighbour_key in neighbours:    # loop on neighbour nods and update their costs
            alt = dist[node_key] + g[node_key][neighbour_key]
            if alt < dist[neighbour_key]:
                dist[neighbour_key] = alt
                prev[neighbour_key] = node_key
                pq.put((alt, neighbour_key))
    return prev, dist[target]


def print_path(pa: dict, start, end):
    path = deque()
    current = end
    while current != start:
        path.appendleft(current)
        current = pa[current]
    print(start)
    for n in path:
        print(n)
    return

print_path(dijkstra_pq(test_graph, "A", "F")[0], "A", "F")
# print_path(dijkstra(test_graph, costs, parents, processed, "A", "F")[0], "A", "F")
