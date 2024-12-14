from collections import deque

def getGraph():
    isDirect = input("The graph is Direct(t/f)?: ").lower() == 't'
    graph = {}
    nodes = int(input("Enter the number of nodes: "))
    
    print("Enter node and neighbors (format: nodeName: [['neighbor1', cost], ...]): ")
    for _ in range(nodes):
        # Split and strip node and neighbor input
        nodeName, neighbors = input().split(":")
        nodeName = nodeName.strip()  # Remove any leading/trailing spaces
        neighbors = neighbors.strip()
        
        if neighbors == "[]":
            graph[nodeName] = []  # No neighbors
        else:
            neighborList = eval(neighbors.strip())
            
            if isDirect:
                graph[nodeName] = neighborList
            else:
                for neighbor, cost in neighborList:
                    if [neighbor, cost] not in graph.setdefault(nodeName, []):
                        graph[nodeName].append([neighbor, cost])
                    if [nodeName, cost] not in graph.setdefault(neighbor, []):
                        graph[neighbor].append([nodeName, cost])
    return graph

def breadth_search(graph, startNode, goalNode):
    # Check for errors
    if not graph:
        return "Error: Invalid graph"
    elif startNode not in graph:
        return "Error: start node not exist"
    elif goalNode not in graph:
        return "Error: goal node not exist"
    
    queue = deque() # 
    closedSet = []  # store visited nodes
    parent = {}  # track predecessors for path reconstruction
    cost = {startNode: 0}  # Dictionary to track cumulative cost to each node

    queue.append(startNode) # {a,}
    parent[startNode] = None  # Start node has no predecessor

    while queue:
        currentNode = queue.popleft()  # Dequeue the first node
        
        if currentNode not in closedSet:  # Add to closed set if not already visited
            closedSet.append(currentNode)
        
        if currentNode == goalNode:  # Check if the goal is reached
            # Get the path using the parent dictionary
            path = []
            while currentNode is not None:
                path.append(currentNode)
                currentNode = parent[currentNode]
            path.reverse()  # Reverse the path to get it from start to goal
            return {
                'closedSet': closedSet,
                'path': path,
                'cost': cost[goalNode]
            }
        
        # Add neighbors to the queue if not already visited
        for neighbor, edge_cost in sorted(graph[currentNode]):  # Unpack neighbor and cost
            if neighbor not in closedSet and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = currentNode  # Set the current node as the predecessor
                cost[neighbor] = cost[currentNode] + edge_cost  # Update cost

    # If goal is not reachable
    return {
        'closedSet': closed_set,
        'no_of_expanded_nodes': len(closed_set),
        'path': None,
        'cost': Non
      }

print("########## WELCOME ##########")

graph = getGraph()
startNode = input("Enter the Start node: ")
goalNode = input("Enter the goal Node: ")
result = breadth_search(graph, startNode, goalNode)

# Output the result
if isinstance(result, str):
    print(result)
elif isinstance(result, dict):
    print("Closed set:", result['closedSet'])
    print("Path:", " -> ".join(result['path'])) if result['path'] else print("No valid path found.")  # المسار
    print("Cost:", result['cost'])
    print("Number of expaned nodes:", len(result['closedSet']), "including goal node")
######################################## End Program ########################################
