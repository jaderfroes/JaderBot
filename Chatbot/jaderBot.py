import dialogflow_v2 as dialogflow
import argparse
from google.api_core.exceptions import InvalidArgument

'''
Usa os dados da RBAC para criação de inteções do JaderBot
'''

'''
=== cria as inteções com os títulos ===
 autenticar a API - https://cloud.google.com/docs/authentication/getting-started
    seta a variável de ambiente:
        $ export GOOGLE_APPLICATION_CREDENTIALS="/home/jader/Documentos/DadosUFPEL/UFPEL/TCC/Chatbot/JaderBot/Chatbot/jaderbot-ufpel-aee61cbe72f7.json"
'''


def topicos_intencoes(titulos_topicos, links_topicos, project_id):
    '''cria as intenções a partir dos tópicos recebidos'''

    for i in range(len(titulos_topicos)):
        display_name = titulos_topicos[i]
        if len(display_name) > 100:  # limite de char para nome de intent
            display_name = display_name[:99]
        create_intent(project_id, display_name, titulos_topicos[i],
                      [links_topicos[i]])


def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()
    
    parent = intents_client.project_agent_path(project_id)
    training_phrases = []
    
    part = dialogflow.types.Intent.TrainingPhrase.Part(
        text=training_phrases_parts)
    training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
    training_phrases.append(training_phrase)


    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)
      
    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(parent, intent)

    print('Intent created: {}'.format(response))


def cria_lista(caminho):  
    ''' le arquivos com os dados e retorna uma lista'''
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
    project_id = 'jaderbot-ufpel'
    titulos_topicos = cria_lista(path_titulos)

    ''' Cria as intents com os titulos dos tópicos'''
    topicos_intencoes(titulos_topicos[0:4], links_topicos[0:4], project_id)
    #  print(len(titulos_topicos))


if __name__ == "__main__":
    main()
