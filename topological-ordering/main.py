from graph import Graph

# Lista de atividades
activities = [
  {
    "title": "Arrumar a cama",
    "dependent": []
  },
  {
    "title": "Fazer meu café da manhã",
    "dependent": [0, 3]
  },
  {
    "title": "Ir para academia",
    "dependent": [1],
  },
  {
    "title": "Escovar os dentes",
    "dependent": [0],
  },
  {
    "title": "Tomar um banho",
    "dependent": [2]
  },
  {
    "title": "Estudo da manhã",
    "dependent": [4]
  },
  {
    "title": "Trabalhar na IC",
    "dependent": [4]
  },
  {
    "title": "Arrumar para faculdade",
    "dependent": [5, 6]
  }
]

g = Graph(len(activities), list(map(lambda x: x["title"], activities)))

# Populando o grafo com as arestas direcionadas de dependências
for b, act in enumerate(activities):
  for a in act["dependent"]:
    g.add_edge(a, b)

# Imprimindo o resultado da ordenação topológica bonitin!!
for i, act in enumerate(g.topological_ordering()):
  print(f"{i+1}. {act};")