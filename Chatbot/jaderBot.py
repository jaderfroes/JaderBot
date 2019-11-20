import dialogflow_v2 as dialogflow
import argparse
from google.api_core.exceptions import InvalidArgument
import random

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


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    # import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))


def teste_agente(entradas, project_id):
    ''' '''
    #frase = []
    #for i in entradas:
        #frase = entradas[i]
    detect_intent_texts(project_id, 0, entradas, 'pt-BR')


def gera_num_aleatorio(n, limite):
    '''gera lista de n numeros aleatórios entre 0 e lim'''

    return random.sample(range(limite), n)


def main():

    titulos_topicos = []
    links_topicos = []
    path_links = 'links_topicos.txt'
    path_titulos = 'titulos_topicos.txt'
    links_topicos = cria_lista(path_links)
    project_id = 'jaderbot-ufpel'
    titulos_topicos = cria_lista(path_titulos)
    titulos_intencoes = []  # titulos que viram intencoes
    links_intencoes = []  # links que serao usados como resposta
    titulos_teste = []  # titulos que simulam entrada de usuário

    indices_aleatorios = gera_num_aleatorio(55, len(titulos_topicos))
    
    for i in range(0, len(titulos_topicos)):
        if i in indices_aleatorios:  # usados para treino do agente
            titulos_intencoes.append(titulos_topicos[i])
            links_intencoes.append(links_topicos[i])
        else:  # usado para testes do agente
            titulos_teste.append(titulos_topicos[i])

    print(len(titulos_teste), "para testes\n", len(titulos_intencoes), "para treino")

    ''' Cria as intents com a lista de titulos dos tópicos'''
    topicos_intencoes(titulos_intencoes, links_intencoes, project_id)
    
    print(80*'>')
    '''Testas as intencoes'''
    print(titulos_teste)
    teste_agente(titulos_teste, project_id)

if __name__ == "__main__":
    main()
