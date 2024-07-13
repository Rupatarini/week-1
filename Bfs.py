def bfs(graph,start_node):
    visited=set()
    queue=queue()
    queue.put[start_node]
    visited.add(start_node)
    while not queue.empty():
        current_node=queue.get()
        print(current_node,end="->")
    for neighbour in graph[current_node]:
        if neighbour not in visited:
           queue.put(neighbour)
           visited.add(neighbour)
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['E'],
    'D':[],
    'E':['F'],
    'F':[]
}
print(graph)
print(graph['A'])
print(graph['D'])
