import pandas as pd

tabela = pd.read_csv('petroleo_certo.csv',delimiter=';')
#DATAFRAME
# print(tabela)
filtro = (tabela['Unidades da Federação']=='Rio de Janeiro3') & (tabela['Localização'] == 'Mar')
filtro2 = tabela['Ano']==2018

for index, row in tabela.iterrows():
    tabela.at[index,'Reservas totais de petróleo (em milhões de barris)'] = float(row['Reservas totais de petróleo (em milhões de barris)'].replace(',','.'))

print(tabela[filtro2]['Reservas totais de petróleo (em milhões de barris)'].sum())
# #for (let i=1;i<=100;i++){ console.log(i) }

# lista_nums = list(range(1,101))
# lista_divisiveis = []
# lista_letras = ['a','b','c','d','e']

# #IF
# # if CONDIÇÃO:
# #     INSTRUÇÃO
# #FOR
# #WHILE

# # ARGS->FUNCTION->RETURN

# lista_nums = [1,3,5,9,13,345346345645, 3456]

# def encontra_divisores(lista, divisor):
#     nova_lista = []
#     for numero in lista:
#         if numero%divisor == 0:
#             nova_lista.append(numero)
#     return nova_lista
    
# print(encontra_divisores(lista_nums,int(input('Qual é o divisor? '))))


#lista_divisiveis[5] = 67

# while numero<=100:
#     lista.append(numero)
#     numero = numero + 1
