from operator import itemgetter, attrgetter
import fileinput

Arretes=[]

Arborescence=[]


for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Arretes.append((int(line[0]),int(line[1]))) 

Arretes=sorted(Arretes)
connexe={}



def CreerGraphe(Graph,Arretes):
    i=1
    Graph={}
#for i in range(1,len(Arretes)-1,1):
    while(i<len(Arretes)-1):
        voisins=[]
        voisins.append(Arretes[i-1][1])
        while(Arretes[i-1][0]==Arretes[i][0]):
            voisins.append(Arretes[i][1])
            i=i+1
        Graph[Arretes[i-1][0]]=voisins
        i=i+1
    return Graph

g={}
G=CreerGraphe(g,Arretes)


print(Arretes[20][0])
print(sorted(Arretes))
print(len(Arretes))
print(G)

fileinput.close()