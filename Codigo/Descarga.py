# -------------------------------------------------------------------------
#                            EXTRACCION DE DATOS                 
# -------------------------------------------------------------------------

from selenium import webdriver
import bs4
import time

def Extrae(a, N):
    Num = []
    for i in range(a,len(N),4):
        x = str(N[i]).split('center;">')
        x = x[1].split('</td>')
        Num += [x[0]]
    return Num
    
browser = webdriver.Firefox()
browser.get('http://baloto.com/filtro-historico-de-resultados.php')

# En las siguientes lineas se guardaran los datos.
Serie, Fecha, Num1, Num2 = [], [], [], []
A = 2016
for i in range(2001, A+1):
    # En la siguiente se selecciona cada casilla desde 2001 hasta 2016.
    browser.find_element_by_xpath("//select[@id='edit-field-a-o-value']/option[text()="+str(i)+"]").click()
    time.sleep(2)
    res = browser.page_source #Extrae el codigo.
    
    gh = bs4.BeautifulSoup(res, "lxml")
    tabla_archivos = gh.find_all('td',{'style':'text-align: center;'})    
     
    N=tabla_archivos
    # Extrae Numero de Serie
    Serie += Extrae(3, N)
    # Extrae Fecha
    Fecha += Extrae(6, N)
    # Extrae sorteo.
    Num1 += Extrae(4, N)
    Num2 += Extrae(5, N)

# SE ESCRIBEN DATOS EN ARCHIVO EN FORMATO MARKDOWN:
g = open("Datos.md","w")
g.write("| SERIE | FECHA | SORTEO1 | SORTEO1 |\n")
g.write("|:---:|:---:|:---:|:---:|\n")
for i in range(len(Serie)):
    g.write("| "+Serie[i]+" | "+Fecha[i]+" | "+ Num1[i]+ " | "+Num2[i]+" |\n")
g.close()

# SE HACE PROCESAMIENTO DE TEXTO
for i in range(len(Num1)):
    Num1[i] = Num1[i].split(' - ')
    Num2[i] = Num2[i].split(' - ')
while ["00", "00", "00", "00", "00", "00"] in Num2:
    Num2.remove(["00", "00", "00", "00", "00", "00"])  
    
# SE ESCRIBEN NUMEROS DE SORTEO EN ARCHIVO SH: 
f=open("Datos.sh","w")  
for i in range(len(Num1)):
    f.write(Num1[i][0]+"\t"+Num1[i][1]+"\t"+Num1[i][2]+"\t"+Num1[i][3]+"\t"+Num1[i][4]+"\t"+Num1[i][5]+"\n")
for i in range(len(Num2)):    
    f.write(Num2[i][0]+"\t"+Num2[i][1]+"\t"+Num2[i][2]+"\t"+Num2[i][3]+"\t"+Num2[i][4]+"\t"+Num2[i][5]+"\n")   
f.close()

h=open("Numero.sh","w") 
Num = []
for i in range(len(Num1)):
    for j in range(6):
        Num += [Num1[i][j]]
for i in range(1, 45+1):
    if i<10:
        abc = Num.count("0"+str(i))
    else:
        abc = Num.count(str(i))
h.write(str(i)+"\t"+str(abc)+"\n")
h.close()