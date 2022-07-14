# :hammer: ETL AirFlow - Datasets Kagle

<img src="/img/dag.png" alt="DAG de execução"/>

#### Processo responsável pelo download e tratamento do dataset 'roche-data-science-coalition/uncover' disponível no Kaggle, utilizando o AirFlow para o processo de ETL.

[Link do Kaggle](https://www.kaggle.com/roche-data-science-coalition/uncover)

## Funcionalidades do projeto


## :hammer: Instalação e execução

 * :hammer: Criação do container docker e inicialização do AirFlow
    - no terminal, dentro da pasta do projeto, executar o comando:
    '''
        docker-compose up airflow-init
    '''
 * :hammer: Criação de imagem docker para configurações adicionais do ambiente
    - no terminal, dentro da pasta do projeto, executar o comando:
    '''
        docker build . --tag extending_airflow:latest
    '''

 * :hammer: Subindo o servidor AirFlow
    - no terminal, dentro da pasta do projeto, executar o comando:
    '''
        docker-compose up
    '''
 
 * Login e senha de aceso : 'airflow'



    
