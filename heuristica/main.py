# Importa os dados e os algoritmos dos outros ficheiros.
from graphs import romania_graph
from heuristics import romania_heuristics
from greedy import busca_gulosa
from a_star import busca_a_estrela

def run_romania_search():
    inicio, objetivo = 'Arad', 'Bucharest'
    
    print(f"=== ROMANIA GRAPH (start: {inicio} -> goal: {objetivo}) ===")
    
    # --- Executa e exibe o resultado da Busca Gulosa ---
    g_path, g_order, g_cost = busca_gulosa(romania_graph, romania_heuristics, inicio, objetivo)
    print(f"[Greedy] path: {' -> '.join(g_path)} | cost: {g_cost} Km")
    print(f"         explored: {' -> '.join(g_order)}")
    
    # --- Executa e exibe o resultado da Busca A* ---
    a_path, a_order, a_cost = busca_a_estrela(romania_graph, romania_heuristics, inicio, objetivo)
    print(f"[A*]     path: {' -> '.join(a_path)} | cost: {a_cost} Km")
    print(f"         explored: {' -> '.join(a_order)}")

if __name__ == "__main__":
    run_romania_search()

