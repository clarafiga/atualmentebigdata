# import mysql.connector

# conexao = mysql.connector.connect(
#  host="cl",
#  user="root",
#  password="",
#  database="filmesdata"
# )
# cursor = conexao.cursor()

# query = "SELECT * FROM ANO"
# cursor.execute(query)

# resultados = cursor.fetchall()

# for linha in resultados:
#  print(linha)

# cursor.close()
# conexao.close()

import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="filmesdata"
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

# query_filmes = "SELECT * FROM filmesatual WHERE ano > 2024"
# dados_filtrados = obter_dados_do_banco(query_filmes)

# if dados_filtrados:
#     for filmes in dados_filtrados:
#         print(filmes)

# print("*"*100)

# query_direcao = "SELECT * FROM filmesatual WHERE Título = 'Parasita'"
# dados_filtradinhos = obter_dados_do_banco(query_direcao)


# if dados_filtradinhos:
#         for filmes2 in dados_filtradinhos:
#             print(filmes2)

# print("*"*100)  

# query_min = "SELECT Duração FROM filmesatual ORDER BY Duração DESC "
# dados_filfil = obter_dados_do_banco(query_min)

# if dados_filfil:
#         for filminho in dados_filfil:
#             print(filminho)

print("*"*100)  

query_gene = "SELECT Gênero FROM filmesatual GROUP BY Gênero and COUNT(*) AS quantidade "
dados_gene = obter_dados_do_banco(query_gene)

if dados_gene:
        for genero in dados_gene:
            print(genero)


