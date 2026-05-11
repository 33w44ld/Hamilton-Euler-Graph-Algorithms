class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        self.num_edges = 0
    
    def add_edge(self, u, v):
        if u != v and self.matrix[u][v] == 0:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1
            self.num_edges += 1
        
    def remove_edge(self, u, v):
        if self.matrix[u][v] == 1:
            self.matrix[u][v] = 0
            self.matrix[v][u] = 0
            self.num_edges -= 1

    def has_edge(self, u, v):
        return self.matrix[u][v] == 1
    
    def get_neighbors(self, u):
        return [v for v in range(self.num_nodes) if self.matrix[u][v] == 1]
    
    def get_degree(self, u):
        return sum(self.matrix[u])