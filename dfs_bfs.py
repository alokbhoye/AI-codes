def DFS(graph, start):
    visited = set()  # keep track of the visited nodes
    stack = [start]  # use a stack to keep track of nodes to visit next

    while stack:
        node = stack.pop()  # get the next node to visit
        if node not in visited:
            visited.add(node)  # mark the node as visited
            print(node, end=' ')  # visit the node (print its value in this case)
            stack.extend(graph[node])  # add the node's neighbors to the stack

# Use the DFS function on a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

DFS(graph, 'A')  # Output: A C F E B D


from collections import deque

def BFS(graph, start):
    visited = set()  # Keep track of the nodes that we've visited
    queue = deque([start])  # Use a queue to implement the BFS

    while queue:
        node = queue.popleft()  # Dequeue a node from front of queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node, end=' ')  # Visit the node (print its value in this case)
            queue.extend(graph[node])  # Enqueue all neighbours

# Use the BFS function on a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

BFS(graph, 'A')  # Output: A B C D E F