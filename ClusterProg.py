import random
from copy import copy
import sys
from operator import itemgetter, attrgetter
from collections import defaultdict
import fileinput
from itertools import permutations

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


def ExisteArreteGraph(Graph,node1,node2):
    for i in range(0,len(Graph[node1])-1):
        if Graph[node1][i]==node2:
            return True
    #Il serait anormal d'avoir une arrete enregistree seulement pour un sommet.
    for y in range(0,len(Graph[node2])-1):
        if Graph[node2][y]==node1:
            sys.stderr.write("Il se peut qu'il y ait une erreur dans les donnees")
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

def GetDegreNode(Graph,node):
    return len(Graph[node])


def GetVoisins(Graph,node):
    return Graph[node]


#Renvoie un sous-graph complet à partir d'un sommet pris dans le Graph.
def GetClique(Graph,node):
    ListeClique=set()
    ListeClique.add(node)
    Voisins=set(Graph[node])
    AllPermutationVoisins=list(permutations(Voisins))
    for Voisins in AllPermutationVoisins:#Plutôt intervertir seulement le premier sommet avec le reste ! 
        print(Voisins)# faire sa propre fonction !
        for v in Voisins:
            VoisinsDuVoisin=set(Graph[v])
            if (len(VoisinsDuVoisin & set(Voisins)))>0 and (len(ListeClique - VoisinsDuVoisin))==0:
                ListeClique.add(v)
        if len(ListeClique)<2:
            ListeClique.add(Voisins[0])
    return list(ListeClique)

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

#Permettrait un eventuel preprocessing
def ClasserParDegree(Graph):
    Classement=[]
    for v in Graph:
        Classement.append((v,GetDegreNode(Graph,v)))
    return sorted(Classement,key=itemgetter(1), reverse=True)

#Permettrait a terme de rajouter des sommets "idealement disposes" autour d'une clique potentielle detectee
def VoisinCliqueFortementConnecte(Graph,cliq,critere):
    ListeArrete=[]
    Liste=[]
    Clique=set(cliq)
    for v in Clique:
        VoisinClique=set(Graph[v])
        for w in (VoisinClique - Clique):
            if len(Clique - set(Graph[w]))<=critere and not(w in Liste):
                Liste.append(w)
                nonAdj_node_cliq=list(Clique - set(Graph[w]))
                for i in nonAdj_node_cliq:
                    ListeArrete.append((w,i))
                return ListeArrete


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

        


#Vérification si les sommets forment bien des cliques
for v in Graph:
    EstUneClique(Graph,v)




