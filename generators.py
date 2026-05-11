import random 
from graph import Graph

def generate_hamiltonian(nodes, saturation):
    if nodes <= 10:
        raise ValueError("Liczba wierzchołków musi być większa niż 10!")
    
    g = Graph(nodes)

    vertices = list(range(nodes))
    random.shuffle(vertices)

    for i in range(nodes):
        u = vertices[i]
        v = vertices[(i + 1) % nodes]
        g.add_edge(u, v)

    max_edges = nodes * (nodes - 1) // 2
    target_edges = int(max_edges * (saturation / 100.0))

    attempts = 0
    while g.num_edges < target_edges and attempts < 10000:
        a, b, c = random.sample(range(nodes), 3)
        if not g.has_edge(a, b) and not g.has_edge(b, c) and not g.has_edge(c, a):
            g.add_edge(a, b)
            g.add_edge(b, c)
            g.add_edge(c, a)
        attempts += 1

    return g

def generate_non_hamiltonian(nodes):
    g = Graph(nodes)
    max_edges = nodes * (nodes - 1) // 2
    target_edges = int(max_edges * 0.5)

    if nodes > 1: 
        available_nodes = list(range(1, nodes))
        attempts = 0

        while g.num_edges < target_edges and attempts < 10000:
            u, v = random.sample(available_nodes, 2)
            if not g.has_edge(u, v):
                g.add_edge(u, v)
            attempts += 1
    
    return g