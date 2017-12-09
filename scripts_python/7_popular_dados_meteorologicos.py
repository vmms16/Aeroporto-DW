import MySQLdb
import datetime
import sys
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="airport")

x = conn.cursor()
a = open("SP - Congonhas.txt", "r")
cabecalho=a.readline()

while True:
    linha=a.readline()
    if linha =="":
        break
    
    linha = linha.replace("////","").split(",")
    
    codigoEstacao = linha[0]
    data = linha[1]
    data = datetime.datetime.strptime(data, "%d/%m/%Y").date()

    hora = linha[2] + ":00"
    

    if linha[4]=="" or linha[5]=="":
        temperatura=""
    else:
        tempMax = float(linha[4])
        tempMin = float(linha[5])
        temperatura = (tempMax + tempMin) / 2
    
    if linha[7]=="" or linha[8]=="":
        umidade=""
    else:
        umidMax = float(linha[7])
        umidMin = float(linha[8])
        umidade = (umidMax + umidMin) / 2
    
    if linha[13]=="" or linha[14]=="":
        pressao=""
    else:
        presaoMax = float(linha[13])
        presaoMin = float(linha[14])
        pressao = (presaoMax + presaoMin) / 2
    
    
    ventoVel = linha[16]
    precTemp = linha[19].strip("\n")
    precipitacao = precTemp
   
    
    x.execute("""INSERT INTO `airport`.`Dados_Meteorologicos`
                    (`id_est`,
                    `data`,
                    `hora`,
                    `pressao`,
                    `temperatura`,
                    `umidade`,
                    `vento`,
                    `precipitacao`
                    )
                    VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s);""", (codigoEstacao,data,hora,pressao,temperatura,umidade,ventoVel,precipitacao ))
    conn.commit()

print("Terminado!")
