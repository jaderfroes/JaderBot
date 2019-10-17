import requests
from bs4 import BeautifulSoup


link_principal = 'https://forum.aprendizagemcriativa.org/c/grupos-de-trabalho'
link_aux = 'https://forum.aprendizagemcriativa.org'  # para concatenar
links = []  # todos os links da page grupos de trabalho
links_categorias = []  # links que interessam para a aplicação
links_topicos = []  # links dos tópicos de cada categoria
titulos_topicos = []  # titulos dos tópicos de cada categoria
aux = []

'''
Faz o crawler dentro dos links de assuntos da categoria 'Grupos de trabalho'
'''

page = requests.get(link_principal)
#  print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('a'):
    links.append(link.get('href'))
    #  print(link.get('href'))

for i in range(9, 19):  # range definido observando o output
    links_categorias.append(links[i])

#  print(links_categorias)

for i in links_categorias:
    aux.append(link_aux + i)

links_categorias = aux
#  print(links_categorias)

''' faz a busca pelos titulos e links de todos
tópicos de cada categoria presente em 'Grupos de trabalho' '''

for categoria in links_categorias:
    page2 = requests.get(categoria)
    #  print(page2.content)
    soup2 = BeautifulSoup(page2.content, 'html.parser')

    for link2 in soup2.find_all('a'):  # pega os links dos topicos
        if '/t/' in link2.get('href'):  # se link2 for de tópico('/t/')
            links_topicos.append(link2.get('href'))
            # print(link2.get('href'))
           
    # pega os titulos dos topicos
    for tag in soup2.find_all("a", class_="title raw-link raw-topic-link"):
        # adiciona texto da class 'a' removendo \n da direita e da esquerda(l/[r]strip)
        titulos_topicos.append(tag.text.rstrip().lstrip())
        # print(tag.text.rstrip().lstrip())

'''for i in links_topicos:
	print(i)
'''

for j in titulos_topicos:
	print(j)


'''
print(titulos_topicos)
print('\n')
print(links_topicos)
'''
