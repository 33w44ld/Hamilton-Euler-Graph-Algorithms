from graph import Graph

def find_eulerian_cycle(graph: Graph):
    
    nodes = graph.num_nodes
    
    if graph.num_edges == 0:
        return None
        
    for u in range(nodes):
        if graph.get_degree(u) % 2 != 0:
            return None  

    temp_graph = Graph(nodes)
    for u in range(nodes):
        for v in graph.get_neighbors(u):
            if u < v:  
                temp_graph.add_edge(u, v)

    start_node = 0
    for u in range(nodes):
        if temp_graph.get_degree(u) > 0:
            start_node = u
            break

    curr_path = [start_node]
    euler_cycle = []

    while curr_path:
        curr_v = curr_path[-1]

        if temp_graph.get_degree(curr_v) > 0:
            neighbor = temp_graph.get_neighbors(curr_v)[0]
            temp_graph.remove_edge(curr_v, neighbor)
            curr_path.append(neighbor)
        else:
            euler_cycle.append(curr_path.pop())

    euler_cycle.reverse()

    if len(euler_cycle) != graph.num_edges + 1:
        return None

    return euler_cycle