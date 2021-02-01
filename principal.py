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


def SupprimerArreteGraph(Graph,Name_node_1,Name_node_2):
    for i in range(0,len(Graph[Name_node_1])-1):
        if Graph[Name_node_1][i]==Name_node_2:
            del Graph[Name_node_1][i]
    for y in range(0,len(Graph[Name_node_2])-1):
        if Graph[Name_node_2][y]==Name_node_1:
            del Graph[Name_node_2][y]
    return Graph


def AjouterArreteGraph(Graph,Name_node_1,Name_node_2):
    Graph[Name_node_1].append(Name_node_2)
    Graph[Name_node_2].append(Name_node_1)
    return Graph

def ListerArreteSupprimee(List,node1,node2):
    List.append((node1,node2))
    return List

def ListerArreteAjoutee(List,node1,node2):
    List.append((node1,node2))
    return List


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




print(Graph)
Graph=SupprimerArreteGraph(Graph,1,2)
print(Graph)

#print(Arretes)
#print(Graph[8][1])
    




