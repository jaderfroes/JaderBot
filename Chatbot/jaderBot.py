import dialogflow_v2
from google.api_core.exceptions import InvalidArgument

'''
Usa os dados da RBAC para criação de entidades e inteções do JaderBot
'''

'''
=== cria as inteções com os títulos ===
 autenticar a API - https://cloud.google.com/docs/authentication/getting-started
    seta a variável de ambiente:
        $ export GOOGLE_APPLICATION_CREDENTIALS="/home/jader/Documentos/DadosUFPEL/UFPEL/TCC/Chatbot/JaderBot/Chatbot/jaderbot-ufpel-aee61cbe72f7.json"

 pegar o 'parent' pq ele indica para qual agente criar a intenção
 Criar no dialogflow as intenções(tutorial) com os titulos dos tópicos

'''

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
# [END auth_cloud_implicit]

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
    #  print(links_topicos)
    #  print(titulos_topicos)
    
    print("chamando implicit")
    implicit()
    
    # conexão com API
    '''
    client = dialogflow_v2.IntentsClient()
    parent = client.project_agent_path('jaderbot-ufpel') 
    
    # TODO: Initialize `intent`:
    intent = {titulos_topicos[0]: 0}
    response = client.create_intent(parent, intent)
    '''


if __name__ == "__main__":
    main()
