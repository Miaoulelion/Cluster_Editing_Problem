import fileinput
import networkx as nx

Arretes=[]
Graph = nx.Graph()

for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Arretes.append((int(line[0]),int(line[1]))) 

fileinput.close()
Graph.add_edges_from(Arretes)
nbrSommetsGraph=len(Graph)

#for v in Graph:
 #   print(str(v) + " : " + str(Graph[v]))

ListeSommetsTraites=set()
UnionClique=False
k=1

#Tant que ce n'est pas une union de clique, on continue
while not UnionClique:
    print(k)
    ListClique=list(nx.enumerate_all_cliques(Graph))
    PlusGrandeClique=ListClique[len(ListClique)-1*k]
    for v in PlusGrandeClique:
        if (len(PlusGrandeClique)-1<Graph.degree[v]):
            VoisinsExterieursCliques=set(nx.neighbors(Graph,v))
            SommetASupprimer=list(VoisinsExterieursCliques-set(PlusGrandeClique))
            if len(set(SommetASupprimer) & ListeSommetsTraites)>0:
                break
            for w in SommetASupprimer:
                Graph.remove_edge(v,w)
        ListeSommetsTraites.add(v)
    k=k+1
    if nbrSommetsGraph==len(ListeSommetsTraites):
        UnionClique=True



#for v in Graph:
 #   print(str(v) + " : " + str(Graph[v]))











