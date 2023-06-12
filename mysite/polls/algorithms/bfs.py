graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = [] # list for visited nodes
queue = [] # initialize a queue

def bfs(visited, graph, node): # function for bfs
    visited.append(node)
    queue.append(node)

    while queue: # loop to visit each node
        m = queue.pop(0)
        print(m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Following is te Breadth-First Search")
bfs(visited, graph, '5') # func calling