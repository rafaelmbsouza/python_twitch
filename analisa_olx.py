import pandas as pd

df = pd.read_csv('anuncios_iphone.csv')

def trata_preco(valor):
    return int(valor.replace('R$ ','').replace('.','').strip())

def encontra_estado(url):
    return url[8:10].upper()

df['valor'] = df['valor'].apply(trata_preco)
df['estado'] = df['url'].apply(encontra_estado)

filtro = df['valor'] > 600

df[filtro].sort_values(['valor'],ascending=True).to_excel('iphones_filtrada.xlsx')
    