#---------------------------------------------------------
#                           CONSULTA
# --------------------------------------------------------

# Se llaman los datos.
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

m = open('Frecuencia.sh', 'r')
lines = m.readlines()
Numero, Frecuencia = [], []
for i in lines:
    Lista = i.split("\t")
    Numero += [Lista[0]]
    Lista[1] = Lista[1].split("\n")
    Frecuencia += [Lista[1][0]]
m.close()

print "Ingrese 1, 2, 3, o 4 segun el dato que desea consultar"
print "1. Que sorteo salio en la serie ________"
print "2. Sorteos que han salido en el ano _________"
print "3. Sorteos que han salido en la fecha ________"
print "4. Cuantas veces ha salido el numero ____ "
resp = input()

if resp==1:
    A =raw_input("Ingrese el numero de serie ")
    for i in range(2, len(Serie)):
        if int(Serie[i])==int(A):
            print "Sorteo1: "+Sorteo1[i]+"Sorteo2: "+Sorteo2[i]
    print "Proceso Terminado"
elif resp==2:
    A =raw_input("Ingrese el ano AAAA (2001 hasta el 2016)")
    AA = int(A) - 2000
    for i in range(2, len(Fecha)):
        Fecha[i] = Fecha[i].split('/')
        if int(Fecha[i][2])== AA:
            print "Sorteo1: "+Sorteo1[i]+"Sorteo2: "+Sorteo2[i]
    print "Proceso Terminado"
elif resp==3:
    A =raw_input("Ingrese la fecha DD/MM/AA ")
    for i in range(2, len(Serie)):
        if Fecha[i]== " "+A+" ":
            print "Sorteo1: "+Sorteo1[i]+"Sorteo2: "+Sorteo2[i]   
    print "Proceso Terminado"
elif resp==4:
    A =raw_input("Ingrese numero de sorteo (1 hasta 45) ")
    for i in range(45):
        if int(A)==int(Numero[i]):
            print "El numero "+Numero[i]+" ha salido "+Frecuencia[i]+" veces."
    print "Proceso Terminado"
else: 
    print "ERROR: Escoja una de las dos opciones: 1, 2, 3 o 4"