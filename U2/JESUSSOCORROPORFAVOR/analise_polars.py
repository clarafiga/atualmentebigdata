

from pathlib import Path
import matplotlib.pyplot as plt
import polars as pl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


PASTA_PARQUET.mkdir(exist_ok=True)
PASTA_GRAFICOS.mkdir(exist_ok=True)


arquivo_filmes = PASTA_DADOS / "filmesatual.csv"
arquivo_origem = PASTA_DADOS / "origematual.csv"

texto_filmes = arquivo_filmes.read_text(encoding="latin1")
filmes_utf8 = PASTA_DADOS / "filmes_utf8.csv"
filmes_utf8.write_text(texto_filmes, encoding="utf-8")

texto_origem = arquivo_origem.read_text(encoding="latin1")
origem_utf8 = PASTA_DADOS / "origematual_utf8.csv"
origem_utf8.write_text(texto_origem, encoding="utf-8")

filmes = pl.read_csv(filmes_utf8, separator=";")
origem = pl.read_csv(origem_utf8, separator=";")


filmes = filmes.select([
    "Título", "Ano", "Duração", "Gênero", "Classificação", "Vezes"
])

filmes = filmes.rename({
    "Título": "titulo",
    "Ano": "ano",
    "Duração": "duracao",
    "Gênero": "genero",
    "Classificação": "classificacao",
    "Vezes": "vezes_assistido"
})

filmes = filmes.with_columns([
    pl.col("titulo").cast(pl.String).str.strip_chars(),
    pl.col("ano").cast(pl.Int64, strict=False),
    pl.col("duracao").cast(pl.Int64, strict=False),
    pl.col("genero").cast(pl.String).str.strip_chars(),
    pl.col("classificacao").cast(pl.Float64, strict=False),
    pl.col("vezes_assistido").cast(pl.Int64, strict=False)
])

filmes = filmes.drop_nulls([
    "titulo", "ano", "duracao", "genero", "classificacao", "vezes_assistido"
])

origem = origem.select(["Direção", "Main Cast", "País"])
origem = origem.rename({
    "Direção": "direcao",
    "Main Cast": "main_cast",
    "País": "pais"
})
origem = origem.with_columns([
    pl.col("direcao").cast(pl.String).str.strip_chars(),
    pl.col("main_cast").cast(pl.String).str.strip_chars(),
    pl.col("pais").cast(pl.String).str.strip_chars()
])

print("Arquivos CSV carregados e preparados!")
print("Quantidade de filmes:", filmes.height)
print("Quantidade de registros de origem:", origem.height)



arquivo_parquet_filmes = PASTA_PARQUET / "filmes.parquet"
arquivo_parquet_origem = PASTA_PARQUET / "origem.parquet"

filmes.write_parquet(arquivo_parquet_filmes)
origem.write_parquet(arquivo_parquet_origem)

print("Arquivos Parquet salvos na pasta 'parquet'!")

filmes = pl.read_parquet(arquivo_parquet_filmes)
origem = pl.read_parquet(arquivo_parquet_origem)


print("\n--- 10 primeiros filmes ---")
print(filmes.head(10))

print("\n--- Quantidade de filmes por gênero ---")
por_genero = (
    filmes.group_by("genero")
    .agg(pl.len().alias("quantidade"))
    .sort("quantidade", descending=True)
)
print(por_genero)

print("\n--- 10 filmes mais longos ---")
mais_longos = filmes.sort("duracao", descending=True).select(["titulo", "duracao"]).head(10)
print(mais_longos)


generos = por_genero["genero"].to_list()
quantidades = por_genero["quantidade"].to_list()

plt.figure(figsize=(10, 6))
plt.barh(generos[::-1], quantidades[::-1])
plt.title("Quantidade de filmes por gênero")
plt.xlabel("Quantidade de filmes")
plt.ylabel("Gênero")
plt.tight_layout()
plt.savefig(PASTA_GRAFICOS / "filmes_por_genero.png", dpi=150)
plt.close()


colunas_numericas = ["ano", "duracao", "classificacao", "vezes_assistido"]
dados_numericos = filmes.select(colunas_numericas).drop_nulls()

matriz_correlacao = []
for coluna_linha in colunas_numericas:
    linha = []
    for coluna_coluna in colunas_numericas:
        valor = dados_numericos.select(
            pl.corr(coluna_linha, coluna_coluna)
        ).item()
        linha.append(valor)
    matriz_correlacao.append(linha)

print("\n--- Matriz de correlação ---")
correlacao_tabela = pl.DataFrame(
    matriz_correlacao,
    schema=colunas_numericas,
    orient="row"
).with_columns(pl.Series("variavel", colunas_numericas))
correlacao_tabela = correlacao_tabela.select(["variavel"] + colunas_numericas)
print(correlacao_tabela)
correlacao_tabela.write_csv(PASTA / "correlacao.csv")

plt.figure(figsize=(8, 6))
imagem = plt.imshow(matriz_correlacao, vmin=-1, vmax=1)
plt.colorbar(imagem, label="Correlação")
plt.xticks(range(len(colunas_numericas)), colunas_numericas, rotation=30, ha="right")
plt.yticks(range(len(colunas_numericas)), colunas_numericas)
plt.title("Correlação entre variáveis numéricas")

for linha in range(len(colunas_numericas)):
    for coluna in range(len(colunas_numericas)):
        plt.text(coluna, linha, f"{matriz_correlacao[linha][coluna]:.2f}",
                 ha="center", va="center")

plt.tight_layout()
plt.savefig(PASTA_GRAFICOS / "correlacao.png", dpi=150)
plt.close()


dados_modelo = filmes.select([
    "ano", "duracao", "classificacao", "vezes_assistido"
]).drop_nulls()

X = dados_modelo.select(["ano", "duracao", "classificacao"]).to_numpy()

y = dados_modelo["vezes_assistido"].to_numpy()

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)
previsoes = modelo.predict(X_teste)

print("\n--- Regressão linear ---")
print("O que o modelo tenta prever: vezes assistido")
print("Informações usadas: ano, duração e classificação")
print("Resultado R² no conjunto de teste:", round(modelo.score(X_teste, y_teste), 3))
print("R² mais perto de 1 geralmente indica melhor ajuste; pode ser negativo.")

resultado_regressao = pl.DataFrame({
    "valor_real": [float(valor) for valor in y_teste],
    "valor_previsto": [float(valor) for valor in previsoes]
})
resultado_regressao.write_csv(PASTA / "resultado_regressao.csv")

pipiplt.figure(figsize=(7, 6))
plt.scatter(y_teste, previsoes)
menor = min(min(y_teste), min(previsoes))
maior = max(max(y_teste), max(previsoes))
plt.plot([menor, maior], [menor, maior])
plt.title("Regressão linear: valor real x previsto")
plt.xlabel("Vezes assistido - valor real")
plt.ylabel("Vezes assistido - valor previsto")
plt.tight_layout()
plt.savefig(PASTA_GRAFICOS / "regressao_linear.png", dpi=150)
plt.close()

print("\nPronto! Veja os arquivos Parquet na pasta 'parquet'.")
print("Veja os gráficos na pasta 'graficos'.")
print("Também foram salvos correlacao.csv e resultado_regressao.csv.")
