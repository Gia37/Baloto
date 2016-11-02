#Importando la tabla desde el archivo Datos.sh
tabla = read.table("Datos.dat")

#------------------------------------------------------------
# suma de los datos historicos de cada una de las balotas
#------------------------------------------------------------
v1 = c(tabla$V1) 
v2 = c(tabla$V2)
v3 = c(tabla$V3)
v4 = c(tabla$V4)
v5 = c(tabla$V5)
v6 = c(tabla$V6)

#------------------------------------------------------------
#Calcula la Media de cada balota
#------------------------------------------------------------

#Calcula la Media de V1, es decir la media de la balota 1
Media = "Media de la primera balota"; Media; mean(v1)

#Calcula la Media de V2, es decir la media de la balota 2
Media = "Media de la segunda balota"; Media; mean(v2)

#Calcula la Media de V3, es decir la media de la balota 3
Media = "Media de la tercera balota"; Media; mean(v3)

#Calcula la Media de V4, es decir la media de la balota 4
Media = "Media de la cuarta balota"; Media; mean(v4)

#Calcula la Media de V5, es decir la media de la balota 5
Media = "Media de la quinta balota"; Media; mean(v5)

#Calcula la Media de V6, es decir la media de la balota 6
Media = "Media de la sexta balota"; Media; mean(v6)

#------------------------------------------------------------
#Calcula la Desviacion Estandar de cada balota
#------------------------------------------------------------

#Calcula la Desviacion estandar de la balota 1
Desviación = "Desviación estandar de la primea balota"; Desviación; sd(v1)

#Calcula la Desviacion estandar de la balota 2
Desviación = "Desviación estandar de la segunda balota"; Desviación; sd(v2)

#Calcula la Desviacion estandar de la balota 3
Desviación = "Desviación estandar de la tercera balota"; Desviación; sd(v3)

#Calcula la Desviacion estandar de la balota 4
Desviación = "Desviación estandar de la cuarta balota"; Desviación; sd(v4)

#Calcula la Desviacion estandar de la balota 5
Desviación = "Desviación estandar de la quinta balota"; Desviación; sd(v5)

#Calcula la Desviacion estandar de la balota 6
Desviación = "Desviación estandar de la sexta balota"; Desviación; sd(v6)

#------------------------------------------------------------
#Calcula el valor minimo de cada balota
#------------------------------------------------------------

#Calcula el valor minimo de la balota 1
Mínimo ="Mínimo de la primera balota"; Mínimo; min(v1) 

#Calcula el valor minimo de la balota 2
Mínimo ="Mínimo de la segunda balota"; Mínimo; min(v2)

#Calcula el valor minimo de la balota 3
Mínimo ="Mínimo de la tercera balota"; Mínimo; min(v3)

#Calcula el valor minimo de la balota 4
Mínimo ="Mínimo de la cuarta balota"; Mínimo; min(v4)

#Calcula el valor minimo de la balota 5
Mínimo ="Mínimo de la quinta balota"; Mínimo; min(v5)

#Calcula el valor minimo de la balota 6
Mínimo ="Mínimo de la sexta balota"; Mínimo; min(v6)

#------------------------------------------------------------
#Calcula el valor maximo de cada balota
#------------------------------------------------------------

#Calcula el valor maximo de la balota 1
Máximo = "Máximo de la primera balota"; Máximo; max(v1)

#Calcula el valor maximo de la balota 2
Máximo = "Máximo de la segunda balota"; Máximo; max(v2)

#Calcula el valor maximo de la balota 3
Máximo = "Máximo de la tercera balota"; Máximo; max(v3)

#Calcula el valor maximo de la balota 4
Máximo = "Máximo de la cuarta balota"; Máximo; max(v4)

#Calcula el valor maximo de la balota 5
Máximo = "Máximo de la quinta balota"; Máximo; max(v5)

#Calcula el valor maximo de la balota 6
Máximo = "Máximo de la sexta balota"; Máximo; max(v6)