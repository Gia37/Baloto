m = open('Frecuencia.dat', 'r')
lines = m.readlines()
Numero, Frecuencia = [], []
for i in lines:
    Lista = i.split("\t")
    Numero += [Lista[0]]
    Lista[1] = Lista[1].split("\n")
    Frecuencia += [Lista[1][0]]
m.close()

for i in range(len(Frecuencia)):  #convirtiendo los string en integer
    Frecuencia[i] = int(Frecuencia[i])

fmar = [] #lista que contiene la frecuencia de balotas que mas se repiten
fmer = [] #lista que contiene la frecuencia de balotas que menos se repiten
bmas = [] #lista que contiene las balotas que mas se repiten
bmes = [] #lista que contiene las balotas que menos se repiten
for i in range(6):
    x = max(Frecuencia)
    fmar += [x]
    bmas += [Numero[Frecuencia.index(x)]]
    Numero[Frecuencia.index(x)]=-1
    Frecuencia[Frecuencia.index(x)]=-1
    
print "Frecuencia que mas se repite: ", fmar
print "Balotas que mas se repite: ",bmas[0],"-",bmas[1],"-",bmas[2],"-",bmas[3],"-",bmas[4],"-",bmas[5], "\n"

while -1 in Frecuencia:
    Frecuencia.remove(-1)
    Numero.remove(-1)
    
for k in range(6):
    x = min(Frecuencia)
    fmer += [x]
    bmes += [Numero[Frecuencia.index(x)]]
    Frecuencia[Frecuencia.index(x)]= "a"
    
print "Frecuencia que menos se repite: ", fmer
print "Balotas que menos se repite: ",bmes[0],"-",bmes[1],"-",bmes[2],"-",bmes[3],"-",bmes[4],"-",bmes[5], "\n"

y=[]
for i in range(len(fmar)):
    for j in range(len(fmer)):
        y+=[str(fmar[i])+"-"+str(fmer[j])+"="+str(int(fmar[i])-int(fmer[j]))]
        print str(fmar[i])+"-"+str(fmer[j])+"="+str(int(fmar[i])-int(fmer[j]))