import pandas
import requests

#usando o pandas e criando um dataframe
sheet = pandas.read_excel('final_sheet_linkedin.xlsx')
#DATAFRAME

filtro = sheet['company']=='bairesdev'
print(sheet[filtro])

#usando o requests e puxando o HTML do G1
r = requests.get('https://g1.globo.com')

source = r.text
print(source.find("Covid"))

#Cadastro de um novo usuário (estruturas de dados: lista e dicionário)
pessoa = {"nome":"jpbelmonte", "idade":28, "cidade":"Rio de Janeiro", "estado":"RJ"}

print('----CADASTRO DO CLIENTE------')
print("O usuário se chama "+pessoa["nome"]+". Ele tem "+str(pessoa["idade"])+" anos.\n Ele mora na cidade de "+pessoa["cidade"]+"/"+pessoa["estado"])

nomes_parentes = ["Rafael", "Carla", "Bernardo", "Carlos"]
print("Os parentes da "+nome+" são: "+", ".join(nomes_parentes))
print(pessoa["idade"])
