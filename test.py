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



print(len(Graph))