tabla = read.table("Datos.sh")
Vec = c(tabla$V1,tabla$V2,tabla$V3,tabla$V4,tabla$V5,tabla$V6)
Media = "Media: "; Media; mean(Vec)
Desviación = "Desviación estandar: "; Desviación; sd(Vec)
Mínimo ="Mínimo: "; Mínimo; min(Vec) 
Máximo = "Máximo: "; Máximo; max(Vec)

