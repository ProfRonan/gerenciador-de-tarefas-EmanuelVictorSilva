lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, tarefa: str):
    if prioridade not in [True, False]:
        raise ValueError("Prioridade inválida")
    
    for item in lista_de_tarefas:
        if item["tarefa"] == tarefa:
            raise ValueError("Tarefa já existe")
    
    nt = {"prioridade": prioridade, "tarefa": tarefa}
    lista_de_tarefas.append(nt)


def remove_tarefas(indices: tuple[int]):
    indices_decrescentes = sorted(indices, reverse=True)
    
    for indice in indices_decrescentes:
        if indice < 0 or indice >= len(lista_de_tarefas):
            raise ValueError("Tarefa não existe")
        
        del lista_de_tarefas[indice]


def encontra_tarefa(tarefa: str) -> int:
    for indice, item in enumerate(lista_de_tarefas):
        if item["tarefa"] == tarefa:
            return indice
    
    raise ValueError("Tarefa não existe")


def ordena_por_prioridade():
    lista_de_tarefas.sort(key=lambda x: (not x["prioridade"], x["tarefa"]))


def get_lista_de_tarefas() -> list[str]:
    texts = []
    
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    
    return texts

