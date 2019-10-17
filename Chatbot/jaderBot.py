

'''
Usa os dados da RBAC para criação de entidades e inteções do JaderBot
'''

# le os arquivos com dados
# cria as inteções com os títulos
# cria as entidades de alguma maneira

titulos_topicos = []
links_topicos = []
aux = []
path_links = 'links_topicos.txt'
path_titulos = 'titulos_topicos.txt'

file_links = open(path_links, 'r')


while(file_links.readline()):  # le o arquivo de links
    links_topicos.append(file_links.readline())

file_links.close()

for link in links_topicos:  # remove '\n' do final
    aux.append(link.rstrip())

file_titulos = open(path_titulos, 'r')
   

while(file_titulos.readline()):  # le o arquivo de titulos
    titulos_topicos.append(file_titulos.readline())

file_titulos.close()
aux.clear()

for titulo in titulos_topicos:  # remove '\n' do final
    aux.append(titulo.rstrip())

titulos_topicos = aux
print(titulos_topicos)

