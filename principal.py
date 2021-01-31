from operator import itemgetter, attrgetter
import fileinput

Arretes=[]
Vertex={}
Arborescence=[]


for line in fileinput.input():
    if line[0].isdigit():
        line=line.split()
        Arretes.append((int(line[0]),int(line[1]))) 

        
connexe={}

for arrete in Arretes:
    arretePrec=()
    if arretePrec!=arrete:
        connexe
        arretePrec=arrete

#print(sorted(Arretes))
print(Arretes)
print(Vertex)

fileinput.close()