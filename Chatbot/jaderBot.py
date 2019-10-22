

'''
Usa os dados da RBAC para criação de entidades e inteções do JaderBot
'''

'''
=== cria as inteções com os títulos ===
Criar no dialogflow as intenções(tutorial) com os titulos dos tópicos

'''
# cria as entidades de alguma maneira


def cria_lista(caminho):  # le arquivos com os dados e retorna uma lista

    arquivo = open(caminho, 'r')
    aux = []
    lista = []
  
    aux = arquivo.readlines()

    for i in aux:
        lista.append(i.rstrip())  # remove '\n' do fim

    arquivo.close()
    return lista


def main():

    titulos_topicos = []
    links_topicos = []
    path_links = 'links_topicos.txt'
    path_titulos = 'titulos_topicos.txt'

    links_topicos = cria_lista(path_links)
    titulos_topicos = cria_lista(path_titulos)
    print(links_topicos)
    print(titulos_topicos)


if __name__ == "__main__":
    main()
