import pandas as pd

df = pd.read_csv('anuncios_iphone.csv')

def trata_preco(valor):
    return int(valor.replace('R$ ','').replace('.','').strip())

def encontra_estado(url):
    return url[8:10].upper()

df['valor'] = df['valor'].apply(trata_preco)
df['estado'] = df['url'].apply(encontra_estado)

df['title'] = df['title'].apply(lambda x: x.upper().replace('IPHONE ','IPHONE_').replace(' PLUS','_PLUS').replace(' PRO','_PRO'))

df['is_iphone'] = df['title'].apply(lambda x: 'IPHONE' in x)

filtro = df['valor'] > 600 & df['is_iphone']

modelos = ['IPHONE_5', 'IPHONE_6', 'IPHONE_7', 'IPHONE_8', 'IPHONE_9', 'IPHONE_X', 'IPHONE_11']

def encontra_modelo(title, modelos):
    for model in modelos:
        if model in title:
            return model
    return 'UNDEFINED'

df['modelo'] = df['title'].apply(lambda x: encontra_modelo(x,modelos))


df[filtro].to_excel('modelos_iphone.xlsx')