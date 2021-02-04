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
a=Graph[1]
print(type(a))
print(Graph[1])
print(Graph)