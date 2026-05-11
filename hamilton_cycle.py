from graph import Graph

def find_hamiltonian_cycle(graph: Graph):
    nodes = graph.num_nodes
    if nodes == 0:
        return None

    path = [-1] * nodes
    
    path[0] = 0
    
    if not _hamilton_backtracking(graph, path, 1):
        return None
        
    return path + [path[0]]

def _hamilton_backtracking(graph: Graph, path: list, pos: int) -> bool:
   
    nodes = graph.num_nodes
    
    if pos == nodes:
        if graph.has_edge(path[pos - 1], path[0]):
            return True
        return False

    for v in range(1, nodes):
        if graph.has_edge(path[pos - 1], v) and (v not in path[:pos]):
            path[pos] = v
            
            if _hamilton_backtracking(graph, path, pos + 1):
                return True
                
            path[pos] = -1
            
    return False