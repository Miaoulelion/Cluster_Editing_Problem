from operator import itemgetter, attrgetter
from collections import defaultdict
import fileinput
import networkx as nx

Arretes=[]
Graph = nx.Graph()

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Arretes.append((int(line[0]),int(line[1]))) 



Graph.add_edges_from(Arretes)


fileinput.close()

#Arretes=sorted(Arretes)


#Graph.add_edges_from(Arretes)
print(list(nx.enumerate_all_cliques(Graph)))


for v in Graph:
    print(Graph[v])

print(Graph[1][2])

#Graph=AjouterArreteGraph(Graph,2,7)
#Graph=SupprimerArreteGraph(Graph,2,8)
UnionClique=True

#Tant que ce n'est pas une union de clique, on continue
while not UnionClique:
    ListClique=nx.enumerate_all_cliques(Graph)
    for v in Graph:
        
    #for v in Graph:
        #if Graph.degree[v]>

    #On parcourt les sommets du graphe et on marque les sommets
    #qui appartiennnet a une clique (eventuellement a condition de supprimer des arretes)
    #for node in Graph:
        #if (len(Graph[node])<4):#ajouter les autres conditions













