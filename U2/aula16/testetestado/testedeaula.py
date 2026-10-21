import pandas as pd
import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="filmesdata"
)
cursor = conexao.cursor()

query = "SELECT * FROM filmesatual"

cursor.execute(query)

resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

cursor.close()
conexao.close()

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
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

# Usando a função
query_filmesgenero = "SELECT * FROM filmesatual "
dados_filtrados = obter_dados_do_banco(query_genero)

if dados_filtrados:
    for gênero in dados_filtrados:
        print(Gênero)


query_filmesatual = "SELECT * FROM ano"
df_ano = pd.DataFrame(obter_dados_do_banco(query_ano), columns=['id_filme', 'titulo', 'ano'])
print(df_filmes)

df_filmes = pd.read_csv('filmesatual.csv')
print(df_filmes)

# Relacionando os DataFrames pela coluna 'id_filme'
df_relacionado = pd.merge(df_filmes, df_ano, on='id_filme', how='inner')

print(df_relacionado)