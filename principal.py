from random import *
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

#Creation du graph (dictionnaire) a partir des input.
Graph=CreerGraphe(Arretes)



def supprimerArete(Graphe, u,v):
    i = 0
    while i < len(Graphe[u]):
        if Graphe[u][i] == v:
            del Graphe[u][i]
        i+=1
    j = 0
    while j < len(Graphe[v]):
        if Graphe[v][j] == u:
            del Graphe[v][j]
        j+=1
    return Graphe



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


def ExisteArreteGraph(Graph,node1,node2):
    for i in range(0,len(Graph[node1])-1):
        if Graph[node1][i]==node2:
            return True
    #Il serait anormal d'avoir une arrete enregistree seulement pour un sommet.
    for y in range(0,len(Graph[node2])-1):
        if Graph[node2][y]==node1:
            print("Il se peut qu'il y ait une erreur dans les donnees")
            return True
    return False

def AjouterArreteGraph(Graph,Name_node_1,Name_node_2):
    if not ExisteArreteGraph(Graph,Name_node_1,Name_node_2):
        Graph[Name_node_1].append(Name_node_2)
        Graph[Name_node_2].append(Name_node_1)
    return Graph

def ListerArreteSupprimee(List,node1,node2):
    List.append((node1,node2))
    return List

def ListerArreteAjoutee(List,node1,node2):
    List.append((node1,node2))
    return List







#Renvoie les voisins d'un sommet et leur % de voisins partages
def GetDegreDeConnexionNode(Graph,node):
    voisins=set(Graph[node])
    nbrVoisin=float(len(voisins))
    ListeDegre=[]
    for v in voisins:
        voisins_2nd=set(Graph[int(v)])
        degSommet=float(len(voisins & voisins_2nd)+1)
        ListeDegre.append((degSommet/nbrVoisin))
    return ListeDegre

def GetDegreNode(Graph,node):
    return len(Graph[node])


def GetVoisins(Graph,node):
    return Graph[node]



def GetClique(Graph,node):
    ListeClique=set()
    ListeClique.add(node)
    Voisins=set(Graph[node])
    for v in Voisins:
        VoisinsDuVoisin=set(Graph[v])
        if (len(VoisinsDuVoisin & Voisins))>0 and (len(ListeClique - VoisinsDuVoisin))==0:
            ListeClique.add(v)
    if len(ListeClique)<2:
        Voisins=list(Voisins)
        if len(Voisins)>1:
            ListeClique.add(Voisins[randint(0,len(Voisins)-1)])
        elif len(Voisins)==1:
            ListeClique.add(Voisins[0])
    return list(ListeClique)


def EstUneClique(Graphe,node):
    voisins=set(Graph[node])
    nbrVoisin=float(len(voisins))
    for v in voisins:
        voisins_2nd=set(Graph[int(v)])
        degSommet=float(len(voisins & voisins_2nd)+1)
        if degSommet/nbrVoisin<1:
            return False
    return True


def ClasserParDegree(Graph):
    Classement=[]
    for v in Graph:
        Classement.append((v,GetDegreNode(Graph,v)))
    return sorted(Classement,key=itemgetter(1), reverse=True)


A=ClasserParDegree(Graph)

for i in A:
    print(i)



UnionClique=False
k=0
while not UnionClique:
    Visite=[]
    for node in Graph:#Faire une copie du graph et supprimer les arrêtes
        #print(node)
        Clique=GetClique(Graph,node)
        #print("premiere")
        for v in Clique:
            #print("deuxieme")
            if len(Clique)-1<GetDegreNode(Graph,v):
                ListeASupprimer=set()
                ListeASupprimer=set(Graph[v])-set(Clique)
                ListeASupprimer=list(ListeASupprimer)
                for w in ListeASupprimer:
                    Graph=SupprimerArreteGraph(Graph,v,w)
                    #print("Arrete en suppression : " + str(v) + " et "+ str(w))
                    #print(Graph)
    if k>10:
        UnionClique=True
    k=k+1
    #print("Nombre de tour :" +str(k))
        
    
B=ClasserParDegree(Graph)
print("*******")
for i in B:
    print(i)

for v in Graph:
    print(EstUneClique(Graph,v))



        


"""
for node in Graph:
    voisins=set(Graph[node])
    nbrVoisin=float(len(voisins))
    print("**********Changement de sommet " + str(node) + "************")
    for v in voisins:
        voisins_2nd=set(Graph[int(v)])
        #print("Nombre voisins communs entre " + str(node) + " et " + str(v) + " est de " + str(len(voisins & voisins_2nd)))
        degSommet=float(len(voisins & voisins_2nd)+1)
        print("Degre de connexion du sommet " + str(v) + " : " + str(degSommet/nbrVoisin))
"""
"""
print(Graph)

print(GetDegreDeConnexionNode(Graph,1))
print(GetClique(Graph,3))
print(EstUneClique(Graph,1))
print(GetVoisins(Graph,1))
print(GetDegreNode(Graph,1))

"""



