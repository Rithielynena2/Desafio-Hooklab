import pandas as pd
import matplotlib.pyplot as plt 

dados = pd.read_json("dados_compras.json")
print(dados.head())

print(dados.isnull().sum())#Quais valores de coluna estão ausentes na lista

total_compras = dados.shape[0] # retorna o valor de quantas linhas tem e [1] colunas
print(f"Todal de compras {total_compras}")

min_valor = dados['Valor'].min() #valor minimo gasto
max_valor = dados['Valor'].max() # valor maximo
print(f"Valor Máximo: {max_valor:.2f} e valor mínimo: {min_valor:.2f}")

soma_valor = dados['Valor'].sum() #somando todos os valores de toda a coluna valor
med_gasto = soma_valor / total_compras # Valor médio gasto
print(f"Média de de valor gasto por compra {med_gasto:.2f}")
print("\n")

# ACHAR PRODUTO COM MAIOR E MENOR VALOR 
valor_maximo = dados['Valor'].iloc[0]
valor_minimo = dados['Valor'].iloc[0]

produto_mais_caro = dados.iloc[0]
produto_mais_barato = dados.iloc[0]


for index, row in dados.iterrows(): # row linhas
    valor_compra = row['Valor']
    

    if valor_compra > valor_maximo:
        valor_maximo = valor_compra
        produto_mais_caro = row 

    if valor_compra < valor_minimo:
        valor_minimo = valor_compra
        produto_mais_barato = row


# todas informações do usuario e compra >> print("Produto mais caro:", produto_mais_caro) 
# somente nome do produto e valor do produto
print(f"Produto mais caro: {produto_mais_caro['Nome do Item']} - R${produto_mais_caro['Valor']:.2f}")
print(f"Produto mais barato: {produto_mais_barato['Nome do Item']} - R${produto_mais_barato['Valor']:.2f}")
print("\n")

# VERIFICAR QUANTIDADE DE COMPRA E VALOR POR GÊNERO
contagem_masculino = 0
contagem_feminino = 0
contagem_outro = 0

gasto_masculino = 0.0
gasto_feminino = 0.0
gasto_outro = 0.0

# Percorrer cada linha do DataFrame
for index, row in dados.iterrows():
    genero = row['Sexo']
    valor_compra = row['Valor']
    
    # Verificar o gênero e atualizar contagens e gastos
    if genero == 'Masculino':
        contagem_masculino += 1
        gasto_masculino += valor_compra
    elif genero == 'Feminino':
        contagem_feminino += 1
        gasto_feminino += valor_compra
    else: 
        contagem_outro += 1
        gasto_outro += valor_compra 


print(f"Total de compras feitas pelo sexo Masculino:{contagem_masculino}")
print(f"Total de compras feitas pelo sexo Feminino: {contagem_feminino}")
print(f"Outro: {contagem_outro}")
print("\n")
# Exibir o valor total gasto em compras por gênero
print("Valor total gasto em compras por gênero:")
print(f"Masculino: R${gasto_masculino:.2f}")
print(f"Feminino: R${gasto_feminino:.2f}")
print(f"Outro: R${gasto_outro:.2f}")



#CALCULAR A MEDIA DA IDADE POR SEXO
soma_idade_masculino = 0
soma_idade_feminino = 0
soma_idade_outro = 0

for index, row in dados.iterrows():
    genero = row['Sexo']
    idade = row['Idade'] 
    

    if genero == 'Masculino':
        soma_idade_masculino += idade

    elif genero == 'Feminino':
        soma_idade_feminino += idade

    else:
        soma_idade_outro += idade


media_idade_masculino = soma_idade_masculino / contagem_masculino 
media_idade_feminino = soma_idade_feminino / contagem_feminino 
media_idade_outro = soma_idade_outro / contagem_outro 

contagem_vazio = dados['Sexo'].isnull().sum()  # Contar valores nulos
print(contagem_vazio) # NÃO TEM CAMPOS NÃO PREENCHIDOS

print(f"Média da idade de compradores Masculinos: {media_idade_masculino:.2f}")
print(f"Média da idade de compradores Femininos: {media_idade_feminino:.2f}")
print(f"Compradores que não preencheram o campo de Sexo: {contagem_outro} sendo a média: {media_idade_outro:.2f}")


#PARÂMETROS
generos = ['Masculino', 'Feminino', 'Outro']
medias_idade = [media_idade_masculino, media_idade_feminino, media_idade_outro]

# GRÁFICO
plt.bar(generos, medias_idade)
plt.title('Média da Idade por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Média da Idade')

plt.show()

