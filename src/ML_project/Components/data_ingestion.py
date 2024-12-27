import sys, os
from src.ML_project.expection import CustomException
from src.ML_project.logger import logging
import pandas as pd
from src.ML_project.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass

class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def Initiate_Data_Ingestion(self):
        try:
            #reading code
            df = read_sql_data()
            logging.info("reading from mysql Database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("data ingesiton is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path)



        except Exception as e:
            raise CustomException(e,sys)