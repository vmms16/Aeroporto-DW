import MySQLdb
import datetime

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="airport")

csv = open("../dados_voos/VRA_do_MÊS_012017.csv", "r", errors='ignore')

linhas = csv.readlines()

contador = 1

lista_queries = []

for i in range(1, len(linhas)-1):
    print(contador)
    contador += 1
    linha = linhas[i].split(";")
    siglaEmpresa = linha[0]
    numerovoo = linha[1]
    di = linha[2]
    tipoLinha = linha[3]
    aeroportoOrigem = linha[4]
    aeroportoDestino = linha[5]

    partidaPrevista = linha[6]
    if (len(partidaPrevista) > 1):
        data_prevista_partida, hora_prevista_partida = partidaPrevista.split()
    else:
	    data_prevista_partida, hora_prevista_partida = (None, None)
    data_prev_part = data_prevista_partida

    partidaReal = linha[7]
    if (len(partidaReal) > 1):
	    data_real_partida, hora_real_partida = partidaReal.split()
    else:
	    data_real_partida, hora_real_partida = (None, None)
    data_real_part = data_real_partida

    chegadaPrevista = linha[8]
    if (len(chegadaPrevista) > 1):
        data_prevista_chegada, hora_prevista_chegada = chegadaPrevista.split()
    else:
	    data_prevista_chegada, hora_prevista_chegada = (None, None)
    data_prev_cheg = data_prevista_chegada

    chegadaReal = linha[9]
    if (len(chegadaReal) > 1):
        data_real_chegada, hora_real_chegada = chegadaReal.split()
    else:
	    data_real_chegada, hora_real_chegada = (None, None)
    data_real_cheg = data_real_chegada

    situacao_coletada = linha[10]

    x = conn.cursor()

    x.execute("""SELECT id FROM airport.Situacao WHERE descricao = %s;""", [situacao_coletada,])
    t_situacao = list(x.fetchall())
    try:
        situacao = t_situacao[0][0]
    except:
        situacao = 3

    if situacao == 1:
      #data_real_part = ""
      #data_real = ""
      justificativa_sigla = linha[11].strip()
      #lista_queries.append("SELECT id FROM airport.justificativas WHERE sigla = %s;" % (justificativa_sigla))
      x.execute("""SELECT id FROM airport.justificativas WHERE sigla = %s;""", [justificativa_sigla,])
      t_justificativa = list(x.fetchall())
      justificativa = t_justificativa[0][0]
      #lista_queries.append("SELECT id FROM airport.empresa_aerea WHERE sigla = %s;" % (siglaEmpresa))
      x.execute("""SELECT id FROM airport.empresa_aerea WHERE sigla = %s;""", [siglaEmpresa,])
      t_id_empresa = list(x.fetchall())
      if (len(t_id_empresa) > 0):
          id_empresa = t_id_empresa[0][0]
      else:
          id_empresa = "160"
      lista_queries.append("""INSERT INTO `airport`.`voo`
                (`numero_voo`,
                `hora_partida_realizada`,
                `hora_partida_prevista`,
                `hora_chegada_realizada`,
                `hora_chegada_prevista`,
                `data_partida_realizada`,
                `data_partida_prevista`,
                `data_chegada_realizada`,
                `data_chegada_prevista`,
                `empresa_aerea`,
                `justificativa`,
                `id_situacao`)
                VALUES
                ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s');""" % (numerovoo, hora_real_partida, hora_prevista_partida, hora_real_chegada, hora_prevista_chegada, data_real_part, data_prev_part, data_real_cheg, data_prev_cheg, id_empresa, justificativa, situacao))
      x.execute("""INSERT INTO `airport`.`voo`
                (`numero_voo`,
                `hora_partida_realizada`,
                `hora_partida_prevista`,
                `hora_chegada_realizada`,
                `hora_chegada_prevista`,
                `data_partida_realizada`,
                `data_partida_prevista`,
                `data_chegada_realizada`,
                `data_chegada_prevista`,
                `empresa_aerea`,
                `justificativa`,
                `id_situacao`)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", [numerovoo, hora_real_partida, hora_prevista_partida, hora_real_chegada, hora_prevista_chegada, data_real_part, data_prev_part, data_real_cheg, data_prev_cheg, id_empresa, justificativa, situacao])

    elif situacao == 2:
        #lista_queries.append("""SELECT id FROM airport.empresa_aerea WHERE sigla = %s;""" % (siglaEmpresa))
        x.execute("""SELECT id FROM airport.empresa_aerea WHERE sigla = %s;""", [siglaEmpresa,])
        t_id_empresa = list(x.fetchall())
        if (len(t_id_empresa) > 0):
            id_empresa = t_id_empresa[0][0]
        else:
            id_empresa = "160"
        lista_queries.append("""INSERT INTO `airport`.`voo`
                    (`numero_voo`,
                    `hora_partida_realizada`,
                    `hora_partida_prevista`,
                    `hora_chegada_realizada`,
                    `hora_chegada_prevista`,
                    `data_partida_realizada`,
                    `data_partida_prevista`,
                    `data_chegada_realizada`,
                    `data_chegada_prevista`,
                    `empresa_aerea`,
                    `justificativa`,
                    `id_situacao`)
                    VALUES
                    ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s');""" % (numerovoo, hora_real_partida, hora_prevista_partida, hora_real_chegada, hora_prevista_chegada, data_real_part, data_prev_part, data_real_cheg, data_prev_cheg, id_empresa, "NULL", situacao))
        x.execute("""INSERT INTO `airport`.`voo`
                    (`numero_voo`,
                    `hora_partida_realizada`,
                    `hora_partida_prevista`,
                    `hora_chegada_realizada`,
                    `hora_chegada_prevista`,
                    `data_partida_realizada`,
                    `data_partida_prevista`,
                    `data_chegada_realizada`,
                    `data_chegada_prevista`,
                    `empresa_aerea`,
                    `justificativa`,
                    `id_situacao`)
                    VALUES
                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (numerovoo, hora_real_partida, hora_prevista_partida, hora_real_chegada, hora_prevista_chegada, data_real_part, data_prev_part, data_real_cheg, data_prev_cheg, id_empresa, None, situacao))
    else:
        #lista_queries.append("""SELECT id FROM airport.empresa_aerea WHERE sigla = %s;""" % (siglaEmpresa))
        x.execute("""SELECT id FROM airport.empresa_aerea WHERE sigla = %s;""", [siglaEmpresa,])
        t_id_empresa = list(x.fetchall())
        if (len(t_id_empresa) > 0):
            id_empresa = t_id_empresa[0][0]
        else:
            id_empresa = "160"
        lista_queries.append("""INSERT INTO `airport`.`voo`
                    (`numero_voo`,
                    `hora_partida_realizada`,
                    `hora_partida_prevista`,
                    `hora_chegada_realizada`,
                    `hora_chegada_prevista`,
                    `data_partida_realizada`,
                    `data_partida_prevista`,
                    `data_chegada_realizada`,
                    `data_chegada_prevista`,
                    `empresa_aerea`,
                    `justificativa`,
                    `id_situacao`)
                    VALUES
                    ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s');""" % (numerovoo, hora_real_partida, hora_prevista_partida, hora_real_chegada, hora_prevista_chegada, data_real_part, data_prev_part, data_real_cheg, data_prev_cheg, id_empresa, "NULL", situacao))
        x.execute("""INSERT INTO `airport`.`voo`
                    (`numero_voo`,
                    `hora_partida_realizada`,
                    `hora_partida_prevista`,
                    `hora_chegada_realizada`,
                    `hora_chegada_prevista`,
                    `data_partida_realizada`,
                    `data_partida_prevista`,
                    `data_chegada_realizada`,
                    `data_chegada_prevista`,
                    `empresa_aerea`,
                    `justificativa`,
                    `id_situacao`)
                    VALUES
                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (numerovoo, hora_real_partida, hora_prevista_partida, hora_real_chegada, hora_prevista_chegada, data_real_part, data_prev_part, data_real_cheg, data_prev_cheg, id_empresa, None, situacao))

    conn.commit()


csv.close()
conn.close()
print("Terminado!")

with open("queries_voo_062017.sql", "w") as h:
    for q in lista_queries:
        h.write(q)
        h.write('\n')
