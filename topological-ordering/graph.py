from typing import List

class Graph:
  def __init__(self, N_vertices: int, titles: List[str]) -> None:
    self.N_vertices = N_vertices

    # Criando um vetor de vértices com o seu título e seus coincidentes
    self.vertices = [
      {"title": titles[i], "coincidents": []} for i in range(N_vertices)
    ]

    self.degrees = [0 for i in range(N_vertices)]

  # Populando o grafo
  def add_edge(self, a: int, b: int) -> None:
    self.vertices[a]["coincidents"].append(b)
    self.degrees[b] += 1

  def topological_ordering(self) -> List[str]:
    queue = []

    # Adicionando todas as tarefas que não dependem de ninguém
    for i in range(self.N_vertices):
      if(self.degrees[i] == 0):
        queue.append(i)

    result = []
    while len(queue) != 0:
      v = queue.pop(0)

      result.append(v)

      for d in self.vertices[v]["coincidents"]:
        self.degrees[d] -= 1
        if(self.degrees[d] == 0):
          queue.append(d)
    
    # Retornando a lista ordenada das tarefas só com seus títulos :)
    return list(map(lambda i: self.vertices[i]["title"], result))