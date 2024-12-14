from heapq import heappush, heappop # the item with the lowest value will be the top of queue

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
                for neighbor, cost in neighborList: # d: [['b',2],['c',1]   ,['e',2]   ,['f',4]]
                    if [neighbor, cost] not in graph.setdefault(nodeName, []):
                        graph[nodeName].append([neighbor, cost])
                    if [nodeName, cost] not in graph.setdefault(neighbor, []):
                        graph[neighbor].append([nodeName, cost])
    return graph

def a_star(graph, startNode, goalNode, heuristic):
    # Check for errors
    if not graph:
        return "Error: Invalid graph"
    elif startNode not in graph:
        return "Error: start node not exist"
    elif goalNode not in graph:
        return "Error: goal node not exist"

    priority_queue = [] # Priority queue: stores (total_cost, current_node, path, current_cost)
    heappush(priority_queue, [0, startNode, [startNode], 0])
    
    closed_set = []  # store visited nodes
    
    while priority_queue:
        total_cost, current_node, path, current_cost = heappop(priority_queue)
        
        # Avoid revisiting nodes
        if current_node in closed_set:
            continue # == skip
        
        closed_set.append(current_node)

        # Check if goal is reached
        if current_node == goalNode:
            return {
                'closedSet': closed_set,
                'no_of_expanded_nodes': len(closed_set),
                'path': path,
                'cost': current_cost
            }

        # Expand neighbors
        for neighbor, cost in sorted(graph[current_node]):
            if neighbor not in closed_set:
                g_cost = current_cost + cost  # Actual cost to reach the neighbor
                h_cost = heuristic[neighbor]
                f_cost = g_cost + h_cost  # Total cost
                heappush(priority_queue, (f_cost, neighbor, path + [neighbor], g_cost))
    
    # If goal is not reachable
    return {
        'closedSet': closed_set,
        'no_of_expanded_nodes': len(closed_set),
        'path': None,
        'cost': None,
    }

def get_heuristic(graph):
    heuristic = {}

    print("Enter the heuristic of the following nodes:")
    for node in graph.keys(): # a,b,c,d,e,f,g,h
        heuristic[node] = int(input(node + ": "))
    
    return heuristic

print("########## WELCOME ##########")
graph = getGraph()
heuristic = get_heuristic(graph)
startNode = input("Enter the Start node: ")
goalNode = input("Enter the goal Node: ")
result = a_star(graph, startNode, goalNode, heuristic)

# Output the result
if isinstance(result, str):
    print(result)
elif isinstance(result, dict):
    print("Closed set:", result['closedSet'])
    print("Path:", " -> ".join(result['path'])) if result['path'] else print("No valid path found.")  # المسار
    print("Cost:", result['cost'])
    print("Number of expaned nodes:", len(result['closedSet']), "including goal node")
######################################## End Program ########################################
parent = {
    'a': None,
    'b': 'a',
    'c': 'b'
}
