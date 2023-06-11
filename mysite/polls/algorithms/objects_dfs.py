
#make a parent relationship(root)
#search for a root node
#if node has no parents assign it to root variable
class Node:
    def __init__(self, name):
        self.name = name


# Set to keep track of visited nodes of graph.
visited = set() 

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        temp = graph[node]
        for neighbour in temp:
            dfs(visited, graph, neighbour)

# Create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")

# Build the graph
graph = {
  nodeA : [nodeB, nodeC],
  nodeB : [nodeD, nodeE],
  nodeC : [nodeF],
  nodeD : [],
  nodeE : [nodeF],
  nodeF : []
}

dfs(visited, graph, nodeA)
