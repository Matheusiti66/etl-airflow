import pandas as pd
from airflow import DAG
from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi
from airflow.operators.python import PythonOperator, BranchPythonOperator


def download_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('roche-data-science-coalition/uncover', './arq')


def unzip_files():
    import zipfile
    with zipfile.ZipFile('./arq/uncover.zip', 'r') as zipref:
        zipref.extractall('./arq/')


def calculate_percentile():
    df = pd.read_excel('./arq/Canada_Hosp_COVID19_Inpatient_DatasetDefinitions/Canada_Hosp1_COVID_InpatientData.xlsx')
    
    percentile = {
        50: [df['age'].quantile(0.5)],
        75: [df['age'].quantile(0.75)],
        90: [df['age'].quantile(0.9)]
    }
    df_percentile = pd.DataFrame(percentile)
    print(df_percentile)


def calculate_ratio():
    df = pd.read_excel('./arq/Canada_Hosp_COVID19_Inpatient_DatasetDefinitions/Canada_Hosp1_COVID_InpatientData.xlsx')
    group = df.groupby('reason_for_admission').size().sort_values(ascending=False).reset_index()
    group = group.rename(columns={'reason_for_admission':'Motivo', 0:'Total'})
    group['razao'] = round(group['Total'] / sum(group['Total'])*100,2)
    print(group.head(2))


with DAG('execution_covid',
         start_date = datetime(2022,1,1),
         schedule_interval = '30 * * * *',
         catchup = False) as dag:
    

    download_dataset = PythonOperator(
        task_id = 'download_dataset',
        python_callable = download_dataset
    )

    unzip_files = PythonOperator(
        task_id = 'unzip_files',
        python_callable = unzip_files
    )

    calculate_percentile = PythonOperator(
        task_id = 'calculate_percentile',
        python_callable = calculate_percentile
    )
    
    calculate_ratio = PythonOperator(
        task_id = 'calculate_ratio',
        python_callable = calculate_ratio
    )

    download_dataset >> unzip_files >> [calculate_ratio, calculate_percentile]
