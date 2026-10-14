import pandas as pd

# 1: LEITURA SEM PERDAS
# Se o CSV está quebrado (como a linha do Lucas Ferrão com 6 colunas em vez de 5),
# nós lemos o arquivo linha por linha e corrigimos o erro de separador decimal.

linhas_corrigidas = []
with open('treinamento_alunos.csv', 'r', encoding='latin1') as file:
    for linha in file:
        partes = linha.strip().split(',')
        
        # Se a linha tem 6 partes, é o erro do '850,00'. Vamos unir a parte 4 e 5.
        if len(partes) == 6:
            # Junta o '850' com '00' usando um ponto
            nova_linha = partes[:3] + [f"{partes[3]}.{partes[4]}"] + [partes[5]]
            linhas_corrigidas.append(nova_linha)
        else:
            linhas_corrigidas.append(partes)

# Criamos o DataFrame a partir da lista corrigida
df = pd.DataFrame(linhas_corrigidas[1:], columns=linhas_corrigidas[0])

print(f"Total de linhas carregadas: {len(df)}")
print(df.head())

# 2: RENOMEAR COLUNAS
df.columns = ['id', 'nome', 'data_nasc', 'mensalidade', 'curso']

# 3: TRATAR ENCODING
# Corrigindo os nomes e cursos que vieram como \xc3\xa9
def fix_encoding(text):
    if pd.isna(text) or text == '': return text
    try:
        # Tenta decodificar o que foi lido como string literal
        return text.encode('latin-1').decode('utf-8')
    except:
        return text

df['nome'] = df['nome'].apply(fix_encoding).str.strip()
df['curso'] = df['curso'].apply(fix_encoding).str.strip()

# 4: LIMPEZA DE CARACTERES
# Em vez de converter direto, limpamos tudo que não é número ou ponto
df['mensalidade'] = (
    df['mensalidade']
    .str.replace('R$', '', regex=False)
    .str.replace('.', '', regex=False) # Remove ponto de milhar
    .str.replace(',', '.')             # Troca vírgula decimal por ponto
    .str.strip()
)

# 5: MUDANÇA DE TIPOS
# Mudamos para numérico. Onde não for possível, ele vira NaN (vazio), mas a LINHA FICA.
df['mensalidade'] = pd.to_numeric(df['mensalidade'], errors='coerce')
df['id'] = pd.to_numeric(df['id'], errors='coerce')

df['data_nasc'] = pd.to_datetime(df['data_nasc'], dayfirst=True, errors='coerce')

# 6: TRATAR VALORES NULOS
# Em vez de dropna(), preenchemos com valores padrão para manter a linha
df['nome'] = df['nome'].replace('', 'NOME NÃO INFORMADO')
df['data_nasc'] = df['data_nasc'].fillna('DATA INVÁLIDA') # Vira string para manter o aviso

# 7: ANALISAR COM DESCRIBE
print("\n--- RESUMO ESTATÍSTICO ---")
# Agora o describe mostrará o outlier de 999.999 mas a linha continua lá
print(df.describe(include='all'))

# 8: LIDAR COM DUPLICADAS
# Em vez de apagar, vamos criar uma coluna que avisa se a linha é repetida
df['is_duplicada'] = df.duplicated(keep=False)


print(df)