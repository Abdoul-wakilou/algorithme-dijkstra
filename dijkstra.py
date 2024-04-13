class GrapheDictionnaire:
    def __init__(self):
        self.graphe = {}

    def ajouter_arete(self, s1, s2, p):
        if s1 in self.graphe and s2 in self.graphe:
            self.graphe[s1][s2] = p

    def ajouter_sommet(self, s):
        if s not in self.graphe:
            self.graphe[s] = {}

    def supprimer_sommet(self, s):
        if s in self.graphe:
            del self.graphe[s]
            for sommet in self.graphe:
                del self.graphe[sommet][s]

    def supprimer_arete(self, s1, s2):
        if s1 in self.graphe and s2 in self.graphe[s1]:
            del self.graphe[s1][s2]

    def recherche(self, s1, s2):
        if s1 in self.graphe and s2 in self.graphe[s1]:
            return self.graphe[s1][s2]
        return None


def dijkstra(graphe, s1):
    sommets = set(graphe.graphe.keys())
    distances = {}
    precedents = {}

    for sommet in sommets:
        distances[sommet] = float('inf')
        precedents[sommet] = None
    distances[s1] = 0

    while sommets:
        sommet = min(sommets, key=lambda s: distances[s])
        sommets.remove(sommet)

        for voisin in graphe.graphe[sommet]:
            if voisin in sommets:
                distance = distances[sommet] + graphe.graphe[sommet][voisin]
                if distance < distances[voisin]:
                    distances[voisin] = distance
                    precedents[voisin] = sommet

    return distances, precedents

graphe = GrapheDictionnaire()
graphe.ajouter_sommet('A')
graphe.ajouter_sommet('B')
graphe.ajouter_sommet('C')
graphe.ajouter_sommet('D')
graphe.ajouter_sommet('E')
graphe.ajouter_sommet('F')
graphe.ajouter_arete('A', 'B', 2)
graphe.ajouter_arete('A', 'C', 10)
graphe.ajouter_arete('B', 'A', 2)
graphe.ajouter_arete('B', 'C', 7)
graphe.ajouter_arete('B', 'D', 3)
graphe.ajouter_arete('B', 'E', 1)
graphe.ajouter_arete('C', 'A', 10)
graphe.ajouter_arete('C', 'B', 7)
graphe.ajouter_arete('C', 'E', 8)
graphe.ajouter_arete('D', 'B', 3)
graphe.ajouter_arete('D', 'E', 3)
graphe.ajouter_arete('D', 'F', 1)
graphe.ajouter_arete('E', 'B', 2)
graphe.ajouter_arete('E', 'C', 8)
graphe.ajouter_arete('E', 'D', 3)
graphe.ajouter_arete('E', 'F', 4)
graphe.ajouter_arete('F', 'D', 1)
graphe.ajouter_arete('F', 'E', 4)

distances, precedents = dijkstra(graphe, 'A')
print(distances)
print(precedents)