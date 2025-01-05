# Importação da Biblioteca Pandas.
import pandas as pd # Importando a biblioteca pandas e atribuindo a variável pd a sua "chamada".

# Leitura/Visualização do Arquivo Excel.
jogos_df = pd.read_excel("Tabela de Jogos.xlsx") # Variável que indica o caminho do arquivo para leitura.
print(jogos_df) # Visualizar o DataFrame.

# Visualização de Dados.
print(jogos_df.head(10)) # Visualizar apenas as 10 primeiras linhas do DataFrame.
print(jogos_df.shape) # Visualizar o tamanho da tabela (linhas X colunas).
print(jogos_df.describe()) # Visualizar um pequeno resumo da tabela.

# Diferença entre Display e Print
# display - Exibe uma informação estilizada na tela (mais recomendado para melhor visualização).
# print - Exibe uma informação não tão estilizada na tela.

# Visualização de Colunas Específicas.
jogos = jogos_df["Jogos"] # Visualizar somente a coluna Jogos (Isso não é um DataFrame, é uma pandas.Series).
jogos__df = jogos_df[["Jogos", "Status"]] # Visualizar somente as colunas Jogos e Status (Isso sim é um DataFrame).

# Visualização de Linhas Específicas.
print(jogos_df.loc[0]) # Pegando apenas uma linha.
print(jogos_df.loc[0:5]) # Pegando da linha 0 até a linha 5.

# Filtragem e Exibição de Dados.
jogos_concluidos_df = print(jogos_df.loc[jogos_df["Status"] == "Concluído"]) # Armazenar jogos que correspondem a uma condição >> (Concluído) << .
jogos_pendentes_df = print(jogos_df.loc[jogos_df["Status"] == "Pendente"]) # Armazenar jogos que correspondem a uma condição >> (Pendente) << .
print(jogos_pendentes_df) # Exibir jogos na tela.

# Visualização de Condições Específicas.
jogos_visualizar_especificos = print(jogos_df.loc[jogos_df["Status"] == "Concluído", ["Jogos", "Gênero", "Nota"]]) # Visualizar condições específicas >> (Concluído) << e colunas específicas >> (Jogos, Gênero, Nota) <<.
print(jogos_visualizar_especificos) # Exibir jogos na tela.
pratica = print(jogos_df.loc[jogos_df["Desenvolvedora"] == "Rocksteady"]) # Exibir apenas a Desenvolvedora Rocksteady.
print(pratica)

# Acesso a Linha e Coluna específica.
print(jogos_df.loc[1, "Jogos"]) # Localizar uma linha e uma coluna específica.
jogos_df.loc[jogos_df["Tempo de Jogo "] == "-", "Tempo de Jogo "] = "" # Localizando uma condição >> (Nota = S.N) << e alterando para >> (-) <<.
print(jogos_df)

# Adição / Remoção de Colunas de um DataFrame
outros_jogos_df = pd.read_excel("Outros Jogos.xlsx") # Variável que indica o caminho do arquivo para leitura (Tabela inexistente, apenas para fins de estudo/anotações).
jogos_df = jogos_df.append(outros_jogos_df) # Variável que adiciona dados de outra tabela ao meu Data Frame (Tabela inexistente, apenas para fins de estudo/anotações).
jogos_df = jogos_df.drop("Notas", axis=1) # (axis=1 remove uma COLUNA, axis=0 remove uma LINHA), e caso a informação axis não esteja presente, o pandas sempre irá excluir uma linha!

# Remoção de Linhas e Colunas Vazias.
jogos_df = jogos_df.dropna(how="all", axis=1) # Deletar LINHAS completamente vazias.
jogos_df = jogos_df.dropna(how="all", axis=0) # Deletar COLUNAS completamente vazias.
jogos_df = jogos_df.dropna(axis=1) # Deletar LINHAS que possuem PELO MENOS 1 valor vazio.

# Preenchimento de Valores Faltantes.
jogos_df["Nota"] = jogos_df["Nota"].fillna(1) # Preencher todas as linhas vazias por 1.

# Preenchimento com Média da Coluna (Não aplicável).
jogos_df["Nota"] = jogos_df["Nota"].fillna([jogos_df["Nota"].mean()]) # Preencher todos os valores vazios com a média da coluna >> (Não se aplica ao caso da nota de um jogo, mas se aplicaria a casos de comissão, por exemplo) <<, e esse código daria erro, já que, na coluna nota, temos strings "-", portanto, não pode-se fazer a média com valores do tipo string.

# Preenchimento com Valor Anterior.
jogos_df = jogos_df.ffill() # É um método que preenche os valores faltantes em uma tabela com o valor anterior. Em outras palavras, se houver uma célula vazia em uma coluna, o método irá preencher essa célula com o valor da célula anterior na mesma coluna.

# Contagem de Desenvolvedoras.
desenvolvedoras = jogos_df["Desenvolvedora"].value_counts() # Conta quantas vezes cada desenvolvedora aparece na tabela.
print(desenvolvedoras) # Exibe o resultado na tela

# Substituição de Valores Vazios.
jogos_df.loc[jogos_df["Tempo de Jogo "] == "", "Tempo de Jogo "] = "0" # Substitui valores vazios em "Tempo de Jogo" por "0".
jogos_df.loc[jogos_df["Nota"] == "", "Nota"] = "0" # Substitui valores vazios em "Nota" por "0".

# Soma de Valores de Jogo (Não aplicável).
soma_tempo_de_jogo = jogos_df.groupby("Jogos").sum() # Tentativa de somar valores de jogo, mas não funcionou devido à falta de uma coluna comum.
print(soma_tempo_de_jogo) # Exibe o resultado (que não é o esperado).

# Mesclando Dados de Diferentes Tabelas.
soma = pd.read_excel("Tabela de Jogos v2.xlsx") # Lê uma tabela de Excel chamada "Tabela de Jogos v2.xlsx" e armazena-a em uma variável chamada soma.
jogos_df = jogos_df.merge(soma) # Mescla a tabela de jogos original com a tabela lida anteriormente e armazena o resultado na variável jogos_df.
print(jogos_df) # Exibe a tabela resultante da mescla no console ou em uma janela de visualização.
