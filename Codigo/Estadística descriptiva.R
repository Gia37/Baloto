#Importando la tabla desde el archivo Datos.sh
tabla = read.table("Frecuencia.sh")

#Suma de todos los valores de V1 hasta V6
Vec = c(tabla$V2)

#Calcula la Media
Media = "Media: "; Media; mean(Vec)

#Calcula la Desviacion estandar
Desviación = "Desviación estandar: "; Desviación; sd(Vec)

#Calcula el minimo
Mínimo ="Mínimo: "; Mínimo; min(Vec) 

#Calcula el maximo
Máximo = "Máximo: "; Máximo; max(Vec)

# Grafico de estadistica de numeros
a <- read.table("Frecuencia.sh")
a
barplot(tabla$V2, main="Estadística de números", xlab="Balotas", col="aquamarine",breaks = 50)

