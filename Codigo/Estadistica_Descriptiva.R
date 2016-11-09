#----------------------------------------------------------------
#                    ESTADÍSTICA DESCRIPTIVA
#----------------------------------------------------------------

#Importando la tabla desde el archivo Datos.dat
tabla = read.table("Datos.dat")

# Balotas
v1 = c(tabla$V1) #Balota1 
v2 = c(tabla$V2) #Balota2
v3 = c(tabla$V3) #Balota3
v4 = c(tabla$V4) #Balota4
v5 = c(tabla$V5) #Balota5
v6 = c(tabla$V6) #Balota6

#------------------------------------------------------------
#Media de cada balota
#------------------------------------------------------------
Media = "Media de la primera balota"; Media; mean(v1)
Media = "Media de la segunda balota"; Media; mean(v2)
Media = "Media de la tercera balota"; Media; mean(v3)
Media = "Media de la cuarta balota"; Media; mean(v4)
Media = "Media de la quinta balota"; Media; mean(v5)
Media = "Media de la sexta balota"; Media; mean(v6)

#------------------------------------------------------------
#Desviacion Estandar de cada balota
#------------------------------------------------------------
Desviación = "Desviación estandar de la primea balota"; Desviación; sd(v1)
Desviación = "Desviación estandar de la segunda balota"; Desviación; sd(v2)
Desviación = "Desviación estandar de la tercera balota"; Desviación; sd(v3)
Desviación = "Desviación estandar de la cuarta balota"; Desviación; sd(v4)
Desviación = "Desviación estandar de la quinta balota"; Desviación; sd(v5)
Desviación = "Desviación estandar de la sexta balota"; Desviación; sd(v6)

#------------------------------------------------------------
# Minimo de cada balota
#------------------------------------------------------------
Mínimo ="Mínimo de la primera balota"; Mínimo; min(v1) 
Mínimo ="Mínimo de la segunda balota"; Mínimo; min(v2)
Mínimo ="Mínimo de la tercera balota"; Mínimo; min(v3)
Mínimo ="Mínimo de la cuarta balota"; Mínimo; min(v4)
Mínimo ="Mínimo de la quinta balota"; Mínimo; min(v5)
Mínimo ="Mínimo de la sexta balota"; Mínimo; min(v6)

#------------------------------------------------------------
# Maximo de cada balota
#------------------------------------------------------------
Máximo = "Máximo de la primera balota"; Máximo; max(v1)
Máximo = "Máximo de la segunda balota"; Máximo; max(v2)
Máximo = "Máximo de la tercera balota"; Máximo; max(v3)
Máximo = "Máximo de la cuarta balota"; Máximo; max(v4)
Máximo = "Máximo de la quinta balota"; Máximo; max(v5)
Máximo = "Máximo de la sexta balota"; Máximo; max(v6)


#Importando la tabla desde el archivo Frecuencia.dat
tabla1 = read.table("Frecuencia.dat")

# DATOS
Num <- c(tabla1$V1) #Numeros
Frec <- c(tabla1$V2) #Frecuencia

Frec = sort(Frec)
Fmas <- c(Frec[45], Frec[44], Frec[43], Frec[42], Frec[41], Frec[40])
Fmen <- c(Frec[1], Frec[2], Frec[3], Frec[4], Frec[5], Frec[6])
"Las mayores frecuencias son"; Fmas
"Las menores frecuencias son"; Fmen
Media = "La media de las frecuencias es"; Media; mean(Frec)
Desviación = "Desviación estandar de las frecuencias es"; Desviación; sd(Frec)
