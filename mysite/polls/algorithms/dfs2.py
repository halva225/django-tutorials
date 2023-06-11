class Node:
    def __init__(self, value, parents, childrens = None):
        self.value = value
        self.parents = parents
        self.children = childrens
    
    def find_first_root(self, node):
        if not node.parents:
            return node
        
        for parent in node.parents:
            root = self.find_first_root(parent)
            if root is not None:
                return root
        
        return None
        
           
visited = set() 

def dfs(visited, node):
    if node not in visited:
        print(node.value)
        visited.add(node)
        for child in node.children:
            dfs(visited, child)

# Create the nodes
root = Node(1, None)
n3 = Node(3, [root])
n7 = Node(7, [root])
n2 = Node(2, [n3])
n4 = Node(4, [n3])
n8 = Node(8, [n4, n7])

# Define the parent-child relationships
root.children = [n3, n7]
n3.children = [n2, n4]
n7.children = [n8]


dfs(visited, n3.find_first_root(n3))

#https://favtutor.com/blogs/depth-first-search-python