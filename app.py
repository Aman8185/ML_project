from src.ML_project.expection import CustomException
from src.ML_project.logger import logging
import sys
import pandas as pd
from src.ML_project.Components.data_ingestion import DataIngestion
from src.ML_project.Components.data_ingestion import DataIngestionConfig


if __name__ == "__main__":
    logging.info("The Execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.Initiate_Data_Ingestion()
        #data_ingestion_config = DataIngestionConfig()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)