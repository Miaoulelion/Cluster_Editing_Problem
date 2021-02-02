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






def SupprimerArreteGraph(Graph,Name_node_1,Name_node_2):
    for i in range(0,len(Graph[Name_node_1])-1):
        if Graph[Name_node_1][i]==Name_node_2:
            del Graph[Name_node_1][i]
    for y in range(0,len(Graph[Name_node_2])-1):
        if Graph[Name_node_2][y]==Name_node_1:
            del Graph[Name_node_2][y]
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

#On donne un graph et un sommet, renvoie true si le sommet peut former une clique
#Car tous ses voisins a les memes voisins. Il ne reste plus qu'a supprimer certaines arretes.
def FormeUneClique(Graphe,node):
    voisins=set(Graph[node])
    nbrVoisin=float(len(voisins))
    for v in voisins:
        voisins_2nd=set(Graph[int(v)])
        degSommet=float(len(voisins & voisins_2nd)+1)
        if degSommet/nbrVoisin<1:
            return False
    return True



Graph=AjouterArreteGraph(Graph,2,7)
Graph=SupprimerArreteGraph(Graph,2,8)
UnionClique=True

#Tant que ce n'est pas une union de clique, on continue
while not UnionClique:
    NodeCliq=[]
    #On parcourt les sommets du graphe et on marque les sommets
    #qui appartiennnet a une clique (eventuellement a condition de supprimer des arretes)
    for node in Graph:
        if FormeUneClique(Graph,node):
            NodeCliq.append(node)


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



print(GetDegreDeConnexionNode(Graph,1))
print(FormeUneClique(Graph,1))
#print("***")
#Graph=SupprimerArreteGraph(Graph,1,2)
#print(Graph)
#print("***")
#Graph=AjouterArreteGraph(Graph,1,2)
#print(Graph)
#print("***")





