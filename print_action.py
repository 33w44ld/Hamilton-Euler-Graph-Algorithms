def run_print_action(graph):
    if not graph:
        print("Brak grafu do wyświetlenia.")
        return 
    
    print(f"\n--- Reprezentacja grafu ---")
    print(f"Wierzchołki: {graph.num_nodes}")
    print(f"Krawędzie: {graph.num_edges}")

    header = "   " + " ".join(f"{i:2}" for i in range(graph.num_nodes))
    print(header)

    for i, row in enumerate(graph.matrix):
        row_str = " ".join(f"{val:2}" for val in row)
        print(f"{i:2} {row_str}")
    print(f"--- Koniec reprezentacji grafu ---\n")