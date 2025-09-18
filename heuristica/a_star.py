from utils import PriorityQueue, reconstruct_path

def busca_a_estrela(mapa, heuristicas, inicio, objetivo):
    """
    Implementa o algoritmo de busca A.
    """
    fila_prioridade = PriorityQueue()
    fila_prioridade.push(heuristicas[inicio], inicio)
    
    predecessor = {inicio: None}
    custo_g = {cidade: float('inf') for cidade in mapa}
    custo_g[inicio] = 0
    
    ordem_expansao = []

    while fila_prioridade:
        cidade_atual = fila_prioridade.pop()
        
        ordem_expansao.append(cidade_atual)

        if cidade_atual == objetivo:
            caminho = reconstruct_path(predecessor, cidade_atual)
            return caminho, ordem_expansao, custo_g[objetivo]

        for vizinho, distancia in mapa.get(cidade_atual, {}).items():
            novo_custo_g = custo_g[cidade_atual] + distancia
            
            if novo_custo_g < custo_g.get(vizinho, float('inf')):
                custo_g[vizinho] = novo_custo_g
                predecessor[vizinho] = cidade_atual
                custo_f = novo_custo_g + heuristicas[vizinho]
                fila_prioridade.push(custo_f, vizinho)

    return None, ordem_expansao, None

