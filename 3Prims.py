import heapq

def prims_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            total_cost += weight
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))

    return total_cost

# User input
graph = {}
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

print("Enter edges in format: source destination weight")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))  # Since the graph is undirected

start_node = input("Enter starting vertex: ")

print("Total cost of Prim's MST:", prims_mst(graph, start_node))

#Without User input

# import heapq

# def prims_mst(graph, start):
#     visited = set()
#     min_heap = [(0, start)]  # (weight, vertex)
#     total_cost = 0

#     while min_heap:
#         weight, u = heapq.heappop(min_heap)
#         if u not in visited:
#             visited.add(u)
#             total_cost += weight
#             for v, w in graph[u]:
#                 if v not in visited:
#                     heapq.heappush(min_heap, (w, v))
    
#     return total_cost

# # Sample undirected weighted graph
# graph = {
#     'A': [('B', 2), ('C', 3)],
#     'B': [('A', 2), ('C', 1), ('D', 1)],
#     'C': [('A', 3), ('B', 1), ('D', 4)],
#     'D': [('B', 1), ('C', 4)]
# }

# print("Prim's MST Total Cost:", prims_mst(graph, 'A'))
