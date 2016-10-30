h = open('Datos.md', 'r')
lines = h.readlines()
Serie, Fecha, Sorteo1, Sorteo2 = [], [], [], []
for i in lines:
    Lista = i.split("|")
    Serie += [Lista[1]]
    Fecha += [Lista[2]]
    Sorteo1 += [Lista[3]]
    Sorteo2 += [Lista[4]]
h.close()

# En esta funcion se pueden hacer distintos tipos de consultas.
# Cual es la frecuencia absoluta del ano ______
# Cuantas veces ha salido el numero _____________
# Que sorteo salio en la fecha __________
# Que sorteo salio en la serie __________

# Num guarda todos los numeros que se han sorteado en el baloto.
Num=[]
for i in range(2, len(Sorteo1)):
    Sorteo1[i] = Sorteo1[i].split(" - ")
    Sorteo2[i] = Sorteo2[i].split(" - ")
    for j in range(6):
        Num+= [int(Sorteo1[i][j]), int(Sorteo2[i][j])]
            
#def F_Abs():
  #  for i in range
    
   # print len(Num)

def Fecha():
    F =raw_input("Ingrese fecha en formato dd/mm/aa sin ningun espacio")
    for i in range(2, len(Fecha)):
        if Fecha[i]==" "+F+" ":
            return Sorteo1[i], Sorteo2[i]
    return 0

#def Consulta:
    