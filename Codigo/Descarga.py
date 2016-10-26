import requests
import bs4

res = requests.get('http://www.baloto.com/filtro-historico-de-resultados.php')
gh = bs4.BeautifulSoup(res.text, "lxml")
tabla_archivos = gh.find_all('td',{'style':'text-align: center;'})

def Extrae(a, N=len(tabla_archivos)):
    Num = []
    for i in range(a,N,4):
        x = str(tabla_archivos[i]).split('center;">')
        x = x[1].split('</td>')
        Num += [x[0]]
    return Num
    
# Extrae Numero de Serie
Serie = Extrae(3)
# Extrae Fecha
Fecha = Extrae(6)
# Extrae sorteo.
Num1 = Extrae(4)
Num2 = Extrae(5)
        
# SE ESCRIBEN DATOS EN ARCHIVO EN FORMATO MARKDOWN:
g = open("Datos.md","w")
g.write("| SERIE | FECHA | NUMERO |\n")
g.write("|:---:|:---:|:---:|\n")
for i in range(len(Serie)):
    g.write("| "+Serie[i]+" | "+Fecha[i]+" | "+ Num1[i]+ " |\n")
    g.write("|  |  | " + Num2[i]+ " |\n")
g.close()

# SE ESCRIBEN NUMEROS DE SORTEO EN ARCHIVO SH: 
for i in range(len(Num1)):
    Num1[i] = Num1[i].split(' - ')
    Num2[i] = Num2[i].split(' - ')
f=open("Datos.sh","w") 
f.write("Num1\tNum2\tNum3\tNum4\tNum5\tNum6\n")
for i in range(len(Num1)):
    f.write(Num1[i][0]+"\t"+Num1[i][1]+"\t"+Num1[i][2]+"\t"+Num1[i][3]+"\t"+Num1[i][4]+"\t"+Num1[i][5]+"\n")
    f.write(Num2[i][0]+"\t"+Num2[i][1]+"\t"+Num2[i][2]+"\t"+Num2[i][3]+"\t"+Num2[i][4]+"\t"+Num2[i][5]+"\n")
f.close()