from operator import itemgetter, attrgetter
from collections import defaultdict
import fileinput

Arretes=[]

#for line in fileinput.input():
    #if line[0].isdigit():
        #line=line.split()
        #Arretes.append((int(line[0]),int(line[1]))) 

#fileinput.close()
print("**")
# Arretes=sorted(Arretes)
# a=set()
# a.add(1)
# a.add(2)

# def CreerGraphe(Arretes):
#     Graph=defaultdict(list)
#     for node1, node2 in Arretes:
#         Graph[node1].append(node2)
#         Graph[node2].append(node1)
#     return Graph

# #Creation du graph (dictionnaire) a partir des input.
# Graph=CreerGraphe(Arretes)


# def GetDegreNode(Graph,node):
#     return len(Graph[node])

liste=[(1,2),(10,5)]
print(liste[:][0])
