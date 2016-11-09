#------------------------------------------------------------------------------
#                          ESTADISTICA DESCRIPTIVA
#------------------------------------------------------------------------------
import numpy as np 

# Se extrae Frecuecia de Frecuencia.dat
def Frecuencia():
    m = open('Frecuencia.dat', 'r')
    lines = m.readlines()
    Frec = []
    for i in lines:
        Lista = i.split("\t")
        Lista[1] = Lista[1].split("\n")
        Frec += [Lista[1][0]]
    m.close()
    return Frec
    
Num = range(1, 45+1) # Numero de balotas.
Frec = Frecuencia() # Frecuencia de balotas.

for i in range(len(Frec)):  #convirtiendo los string en integer
    Frec[i] = int(Frec[i])

fmar = [] #lista que contiene la frecuencia de balotas que mas se repiten
fmer = [] #lista que contiene la frecuencia de balotas que menos se repiten
bmas = [] #lista que contiene las balotas que mas se repiten
bmes = [] #lista que contiene las balotas que menos se repiten

for i in range(6):
    x = max(Frec)
    fmar += [x]
    bmas += [Num[Frec.index(x)]]
    Num[Frec.index(x)]=-1
    Frec[Frec.index(x)]=-1
    
print "Balotas que mas se repiten: ", bmas[0],"-",bmas[1],"-",bmas[2],"-",bmas[3],"-",bmas[4],"-",bmas[5]

while -1 in Frec:
    Frec.remove(-1)
    Num.remove(-1)
    
for k in range(6):
    x = min(Frec)
    fmer += [x]
    bmes += [Num[Frec.index(x)]]
    Frec[Frec.index(x)]= "a"
    
print "Balotas que menos se repiten: ",bmes[0],"-",bmes[1],"-",bmes[2],"-",bmes[3],"-",bmes[4],"-",bmes[5], "\n"


#------------------------------------------------------------------------------
#                       ESTADISTICA INFERENCIAL
#------------------------------------------------------------------------------


# DEMOSTRACION 1:
#------------------------------------------------------------------------------
def Sorteos():
    h = open('Datos.dat', 'r')
    lines = h.readlines()
    Sorteos = []
    for i in lines:
        Lista = i.split("\t")
        Lista[5] = Lista[5].split("\n")
        Sorteos += [[int(Lista[0]), int(Lista[1]), int(Lista[2]), int(Lista[3]), int(Lista[4]),int(Lista[5][0])]]
    h.close()
    return Sorteos    

S = Sorteos() #Todos los sorteos jugados.

suma = 0 
for i in range(len(S)):
    if bmas[0] in S[i] and bmas[1] in S[i] and bmas[2] in S[i]:
        suma += 1
        
print "Las 3 balotas que mas se repiten aparece juntas en", suma, "sorteos de", len(S), "\n"

# DEMOSTRACION 2: PROBABILIDAD
#------------------------------------------------------------------------------
Frec1 = Frecuencia()
suma1=0.0
for i in range(len(Frec1)):
    Frec1[i] = int(Frec1[i])
    suma1 += Frec1[i]

Prob = []
for i in range(len(Frec1)):
    Prob += [Frec1[i]/suma1*100] #Probabilidad de cada balota de salir.
    print "La probabilidad de la balota", i+1, "es:", Prob[i], "%"
print ""

Prob = np.array(Prob)
Media = Prob.mean()

suma2=0
for i in range(len(Prob)):
    suma2 += abs(Prob[i]-Media)
DesvMedia = suma2/float(len(Frec1))

print "La media aritmetica de las probabilidades es: ", Prob.mean()
print "La desviacion media es: ", DesvMedia 

# DEMOSTRACION 3: DIFERENCIA DE BALOTAS CON MAYOR Y MENOR FRECUENCIA.
#------------------------------------------------------------------------------
y=[]
for i in range(len(fmar)):
    for j in range(len(fmer)):
        y+=[int(fmar[i])-int(fmer[j])]
        
print "\nLas diferencias entre el sorteo de mayor frecuencia con la menor es", y
print "La mayor diferencia:", max(y), "y la menor diferencia:", min(y)