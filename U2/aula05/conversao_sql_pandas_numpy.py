import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vendas_online"
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

query_produtos = "SELECT * FROM Produtos"
dados_filtrados = obter_dados_do_banco(query_produtos) # <<<< Aqui você chama a função para obter os dados do banco e armazenar o que será convertido em um DataFrame do Pandas. 

df_produtos = pd.DataFrame(dados_filtrados, columns=['id', 'nome_produto', 'preco', 'categoria']) # Consulta em SQL já convertida
print(df_produtos.head()) # Verificar os dados carregados no DataFrame

precos_array = df_produtos['preco'].to_numpy() # Convertendo a coluna 'preco' do DataFrame para um array NumPy

precos_array_final = np.array(precos_array).astype(float) # Convertendo os preços para float, por estarem vindo do banco de dados como string (ex: Decimal('1250.00'))
print(precos_array_final) # Verificar os preços convertidoos; estando tudo OK, podemos utilizar o array pra iniciar a análise estatística e visualização dos dados.

