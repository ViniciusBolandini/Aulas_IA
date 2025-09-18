from utils import PriorityQueue, reconstruct_path, path_cost

def busca_gulosa(mapa, heuristicas, inicio, objetivo):
    """
    Implementa o algoritmo de Busca Gulosa (Greedy Best-First Search).
    """
    fila_prioridade = PriorityQueue()
    fila_prioridade.push(heuristicas[inicio], inicio)
    
    predecessor = {inicio: None}
    cidades_visitadas = set()
    ordem_expansao = []

    while fila_prioridade:
        cidade_atual = fila_prioridade.pop()
        
        if cidade_atual in cidades_visitadas:
            continue
        
        cidades_visitadas.add(cidade_atual)
        ordem_expansao.append(cidade_atual)

        if cidade_atual == objetivo:
            caminho = reconstruct_path(predecessor, cidade_atual)
            custo = path_cost(mapa, caminho)
            return caminho, ordem_expansao, custo

        for vizinho in mapa.get(cidade_atual, {}):
            if vizinho not in predecessor:
                predecessor[vizinho] = cidade_atual
                fila_prioridade.push(heuristicas[vizinho], vizinho)

    return None, ordem_expansao, None

