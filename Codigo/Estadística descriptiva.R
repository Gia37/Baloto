#Importando la tabla desde el archivo Datos.sh
tabla = read.table("Datos.sh")

#Suma de todos los valores de V1 hasta V6
Vec = c(tabla$V1,tabla$V2,tabla$V3,tabla$V4,tabla$V5,tabla$V6)

#Calcula la Media
Media = "Media: "; Media; mean(Vec)

#Calcula la Desviacion estandar
Desviación = "Desviación estandar: "; Desviación; sd(Vec)

#Calcula el minimo
Mínimo ="Mínimo: "; Mínimo; min(Vec) 

#Calcula el maximo
Máximo = "Máximo: "; Máximo; max(Vec)

