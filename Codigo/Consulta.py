#---------------------------------------------------------
#                           CONSULTA
# --------------------------------------------------------

# Funcion que extrae los datos.
def Datos():
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
    
    return Serie, Fecha, Sorteo1, Sorteo2, Numero, Frecuencia

# Funcion consulta.
def Consulta():
    S, F, S1, S2, Num, Frec = Datos()
    print "Ingrese 1, 2, 3, o 4 segun el dato que desea consultar"
    print "1. Sorteo que salio en la serie "
    print "2. Sorteos que han salido en el a?o "
    print "3. Sorteos que han salido en la fecha "
    print "4. Cuantas veces ha salido el numero  "
    resp = input()
    
    if resp==1:
        A =raw_input("Ingrese el numero de serie ")
        for i in range(2, len(S)):
            if int(S[i])==int(A):
                return 1, [S1[i], S2[i]]
        return 1, "ERROR: Dato no encontrado."
    elif resp==2:
        A =raw_input("Ingrese el a?o AAAA (2001 hasta el 2016)")
        AA = int(A) - 2000
        x = []
        for i in range(2, len(F)):
            F[i] = F[i].split('/')
            if int(F[i][2])== AA:
                x += [S1[i], S2[i]]
        if x!=[]:
            return 2, x
        else:
            return 2, "ERROR: Dato no encontrado."
    elif resp==3:
        A =raw_input("Ingrese la fecha DD/MM/AA ")
        for i in range(2, len(S)):
            if F[i]== " "+A+" ":
                return 3, [S1[i], S2[i]]
        return 3, "ERROR: Dato no encontrado."
    elif resp==4:
        A =raw_input("Ingrese numero de sorteo (1 hasta 45) ")
        for i in range(45):
            if int(A)==int(Num[i]):
                return 4, [Num[i], Frec[i]]
        return 4, "ERROR: Dato no encontrado."
    else: 
        return 0, "ERROR: Escoja una de las opciones: 1, 2, 3 o 4"
        

# Funcion formato markdown        
def F_Mark(N, R_T):
    N, R_T = Consulta()
    Resp = ""
    if type(R_T)==list:
        if N!=4:
            Resp += "|Baloto|Revancha|\n|:---:|:---:|\n"
        else:
            Resp += "|Num|Frecuencia|\n|:---:|:---:|\n"
        for i in range(0, len(R_T), 2):
            Resp += "|"+R_T[i]+"|"+R_T[i+1]+"| \n"
        return Resp
    else:
        return R_T   
        
# Respuesta en la terminal:
def R_Ter(N, R_T):
    N, R_T = Consulta()
    if type(R_T)==list:
        for i in range(0, len(R_T), 2):
            if N!=4:
                print "Baloto :"+R_T[i]+" Revancha: "+R_T[i+1]
            else: 
                print "El Num "+R_T[i]+" ha salido "+R_T[i+1]+ " veces"
        return ""
    else:
        return R_T

print R_Ter(Consulta())