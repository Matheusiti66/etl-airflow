#  ETL AirFlow - Datasets Kagle

<img src="/img/dag.png" alt="DAG de execução"/>

#### Processo responsável pelo download e tratamento do dataset 'roche-data-science-coalition/uncover' disponível no Kaggle, utilizando o AirFlow para o processo de ETL.

[Link do Kaggle](https://www.kaggle.com/roche-data-science-coalition/uncover)


## Funcionalidades do projeto

 *Funções - arquivo dags/execution_covid.py
    - download_dataset: Responsável por autenticar e fazer o download do dataset utilizando a api do Kaggle.
    - unzip_files: Responsável por descompactar o arquivo baixado na task anterior.
    - calculate_percentile: Faz o calculo dos percentís 50, 75 e 90, utilizando o metodo quantile da biblioteca Pandas.
    - calculate_ratio: Faz o calculo da razão de admissão, utilizando funcionalidades da biblioteca Pandas.
    - Objeto DAG: Responsável por configurar todos os passos de execução do processo de ETL.

## :hammer: Instalação e execução

 *  Criação do container docker e inicialização do AirFlow
    - no terminal, dentro da pasta do projeto, executar o comando:
    '''
        docker-compose up airflow-init
    '''
 *  Criação de imagem docker para configurações adicionais do ambiente
    - no terminal, dentro da pasta do projeto, executar o comando:
    '''
        docker build . --tag extending_airflow:latest
    '''

 *  Subindo o servidor AirFlow
    - no terminal, dentro da pasta do projeto, executar o comando:
    '''
        docker-compose up
    '''

 * Login e senha de aceso : 'airflow'



    
