from src.ML_project.expection import CustomException
from src.ML_project.logger import logging
import sys
import pandas as pd
from src.ML_project.Components.data_ingestion import DataIngestion
from src.ML_project.Components.data_ingestion import DataIngestionConfig
from src.ML_project.Components.Data_transformation import DataTransformationConfig
from src.ML_project.Components.Data_transformation import Data_Transformation


if __name__ == "__main__":
    logging.info("The Execution has started")

    try:

        data_ingetion = DataIngestion()

        train_path, test_path = data_ingetion.Initiate_Data_Ingestion()

        data_transformation = Data_Transformation()
        data_transformation.initiate_data_transformation(train_path, test_path)




        # data_ingestion=DataIngestion()
        # data_ingestion.Initiate_Data_Ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)