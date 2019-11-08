# JaderBot

## Dialogflow
    https://cloud.google.com/dialogflow/docs/api-overview
    1- Instalação da biblioteca
        pip install --user dialogflow


### Intenções

### Entidades

### Webhook

### Flask
1-Instalar o flask para fazer a conexão da API com o app;
2-Executar
```
{
    $pip install --user flask
    python app.py or FLASK=hello.py flask run
}
```
### Django
1- Instalar o Django .
2- criar projeto 'djangotest'.
3- aplicar migrações para o app.
4- cria o aplicativo 'myapp' para o webhook.
```
{
    $pip install --user Django
    $django-admin startproject djangotest
    $python manage.py migrate
    $python manage.py startapp myapp
}
```

### Conexão com a API
1- autenticar a API - https://cloud.google.com/docs/authentication/getting-started
                    - https://cloud.google.com/dialogflow/docs/quick/api#detect-intent-text-python
    seta a variável de ambiente no mesmo 'terminal' do SDK:
        $ export GOOGLE_APPLICATION_CREDENTIALS="/home/jader/Documentos/DadosUFPEL/UFPEL/TCC/Chatbot/JaderBot/Chatbot/jaderbot-ufpel-aee61cbe72f7.json"

    instalar biblioteca para autenticação
    $ pip install --upgrade google-cloud-storage

    inicializa o google SDK:
        $ ./Downloads/google-cloud-sdk/bin/gcloud init

    apontou para o projeto [n] utilizado
    
    na aba do SDK, testa o google SDK:
        gcloud auth application-default print-access-token

    ele retorna uma credencial: 
    ya29.c.Kl6wB9YI505jtVyGQWUhgahI-OoLJ0z6TXtCvwd4ITSkvBhmNDcL6EIKlSIsMksS3Js6OpL3ZWjNU3_xbekMiwPcMPQlUlOBlv8LR84Cr7RkIBiy4-GgijXve_120Ldz


