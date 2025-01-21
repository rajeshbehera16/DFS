graph = {
   'A': ['B', 'C', 'D'],
   'B': ['E', 'F'],
   'C': ['G'],
   'D': [],
   'E': [],
   'F': [],
   'G': []
}
start_node = 'A'
visited = set() 
stack = [start_node] 
 

print("DFS Traversal Order:")
while stack:
   current_node = stack.pop() 
   if current_node not in visited:
       print(current_node, end=" ") 
       visited.add(current_node) 
       for neighbor in reversed(graph[current_node]):
           if neighbor not in visited:
               stack.append(neighbor)