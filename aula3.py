#REQUESTS -> FAZER REQUISIÇÕES HTTP (URLLIB3)
#HTTP = Hypertext Transfer Protocol
#BEAUTIFULSOUP -> HTML ou XML -> Organiza-lo de maneira a ler no python
#PANDAS -> pegar esses objetos e tranformar em EXCEL

#USAR REQUESTS E ENTENDER COMO FUNCIONA.

import requests as req

url = 'https://g1.globo.com'

r = req.get(url)

conteudo_cru = r.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(conteudo_cru, 'lxml')
noticias = soup.find_all('div','bastian-feed-item')

for noticia in noticias:
    #imprime informação básica
    titulo = noticia.find('a','feed-post-link').text
    url = noticia.find('a','feed-post-link')['href']
    data = noticia.find('span','feed-post-datetime').text
    print('\n\n'+data+'\n'+titulo+'\nAcesse em: '+url)

    #faz segunda requisição
    r2 = req.get(url)
    soup2 = BeautifulSoup(r2.content, 'lxml')
    t = soup2.find('time').text
    print('\n'+t+'\n')
    article = soup2.find('div','mc-article-body').text
    print(article+'\n')
