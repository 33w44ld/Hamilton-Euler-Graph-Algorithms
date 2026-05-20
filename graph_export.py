def run_export_action(graph):
    """Generuje kod TikZ dla grafu nieskierowanego."""
    if not graph:
        print("Brak grafu do eksportu.")
        return

    print("\n% Skopiuj poniższy kod do swojego sprawozdania w LaTeX.")
    print("% Wymaga kompilacji w LuaLaTeX!")
    print("% Dodaj w preambule:")
    print("% \\usepackage{tikz}")
    print("% \\usetikzlibrary{graphs, graphdrawing}")
    print("% \\usegdlibrary{force}")
    print("\n\\begin{tikzpicture}[>=stealth]")
    
    print("  \\graph [")
    print("    spring layout,")
    print("    nodes={circle, draw, fill=blue!20, minimum size=7mm},")
    print("    node distance=1.5cm")
    print("  ] {")
    
    connected_nodes = set()
    
    for u in range(graph.num_nodes):
        neighbors = graph.get_neighbors(u)
        for v in neighbors:
            if u < v:
                print(f"    {u} -- {v};")
                connected_nodes.add(u)
                connected_nodes.add(v)
                
    for u in range(graph.num_nodes):
        if u not in connected_nodes:
            print(f"    {u};")
                
    print("  };")
    print("\\end{tikzpicture}\n")