import sys
from collections import defaultdict
import fileinput

Graph=defaultdict(list)

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Graph[int(line[0])].append(int(line[1]))
        Graph[int(line[1])].append(int(line[0])) 
        
        
fileinput.close()


def SupprimerArreteGraph(Graph,Name_node_1,Name_node_2):
    for i in range(0,len(Graph[Name_node_1])):
        if Graph[Name_node_1][i]==Name_node_2:
            del Graph[Name_node_1][i]
            break
    for y in range(0,len(Graph[Name_node_2])):
        if Graph[Name_node_2][y]==Name_node_1:
            del Graph[Name_node_2][y]
            break
    return Graph

def GetDegreNode(Graph,node):
    return len(Graph[node])

#Renvoie le plus grand sous-graph complet à partir d'un sommet pris dans le Graph.
def GetClique(Graph,node):
    Voisins=Graph[node]
    ListeCopie=[]
    for i in range(0,len(Voisins)): 
        ListeClique=set()
        ListeClique.add(node)
        Voisins.insert(0,Voisins.pop())
        for v in Voisins:
            VoisinsDuVoisin=set(Graph[v])
            if (len(ListeClique - VoisinsDuVoisin))==0:
                ListeClique.add(v)
        if len(ListeClique)>len(ListeCopie):
            ListeCopie=list(ListeClique)
    return ListeCopie

#Vérification des degrés des sommets et des sommets communs
#Permet de vérifier sommairement si les sommets visités sont bien dans une clique.
def EstUneClique(Graphe,node):
    voisins=set(Graph[node])
    nbrVoisin=float(len(voisins))
    for v in voisins:
        voisins_2nd=set(Graph[v])
        degSommetCommun=float(len(voisins & voisins_2nd)+1)
        degSommet=float(len(voisins_2nd))
        if degSommet/nbrVoisin!=1.0 or degSommetCommun/nbrVoisin!=1.0:
            sys.stderr.write("Ce n'est pas une clique : " + str(node) + "\n")
            return False
    return True


SommetsVisites=[]

#Algo principale de suppression des arrêtes
#autour des cliques potentielles
for s in Graph:
    if s not in SommetsVisites:
        Clique=GetClique(Graph,s)
        SommetsVisites.append(s)
        for v in Clique:
            if len(Clique)-1<GetDegreNode(Graph,v):
                ListeASupprimer=set()
                ListeASupprimer=set(Graph[v])-set(Clique)
                ListeASupprimer=list(ListeASupprimer)
                for w in ListeASupprimer:
                    Graph=SupprimerArreteGraph(Graph,v,w)
                    print(str(v)+ " "+str(w))


#Vérification si les sommets du graph forment bien des unions de cliques
for v in Graph:
    EstUneClique(Graph,v)




