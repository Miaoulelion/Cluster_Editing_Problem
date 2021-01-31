from operator import itemgetter, attrgetter
from collections import defaultdict
import fileinput

Arretes=[]

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Arretes.append((int(line[0]),int(line[1]))) 

fileinput.close()
Arretes=sorted(Arretes)


def CreerGraphe(Arretes):
    Graph=defaultdict(list)
    for node1, node2 in Arretes:
        Graph[node1].append(node2)
        Graph[node2].append(node1)
    return Graph

Graph=CreerGraphe(Arretes)


for node in Graph:
    voisins=set(Graph[node])
    nbrVoisin=float(len(voisins))
    print("**********Changement de sommet************")
    for v in voisins:
        voisins_2nd=set(Graph[int(v)])
        print("Nombre voisins communs entre " + str(node) + " et " + str(v) + " est de " + str(len(voisins & voisins_2nd)))
    #print(type(voisin))
    #for VoisinDuVoisin in voisin:

    #print(voisin)



#print(Arretes)
print(Graph)
#print(Graph[8][1])
    




