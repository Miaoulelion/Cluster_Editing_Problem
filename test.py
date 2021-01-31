from collections import defaultdict

arretes=[(1,2),(1,3),(1,4),(2,3),(8,2),(9,1)]

i=0
dico=defaultdict(list)

for i in range(0,10):
    y=0
    while(y<3):
        y=y+1
        i=i+1
    print(i)


for e1, e2 in arretes:
    dico[e1].append(e2)


print(dico[1][2])


def CreerGraphe(Arretes):
    i=1
    Graph={}
    Arretes=sorted(Arretes)
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


