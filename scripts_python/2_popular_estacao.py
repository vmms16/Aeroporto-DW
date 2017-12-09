import MySQLdb
import os

diretorio = "/home/d3jota/UFRPE/BSI/7_periodo/Datawarehousing/Aeroporto-DW/scripts_python/database-dw/"

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="airport")

for root, dirs, filenames in os.walk(diretorio):
    for f in filenames:
        f = open(os.path.join(diretorio, f), 'r')
        linhas = f.readlines()
        print(f)
        if len(linhas) > 1:
            primeira_linha = linhas[1].split(",")
            codigo = primeira_linha[0]
            print(codigo)
            x = conn.cursor()
            x.execute("""INSERT INTO `airport`.`estacao` (`id`) VALUES (%s)""", [codigo])
            conn.commit()
        else:
            print("tam 1")


conn.close()
