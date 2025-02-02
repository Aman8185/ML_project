import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
    
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgBoost import XGBRegressor



from src.ML_project.expection import CustomException

from src.ML_project.logger import logging



@dataclass

class ModelTrainerConfig:
    trainer_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split Training and test input data")

            X_train, y_train, X_test, y_test=(
                train_array[]
            )
            




        except Exception as e:
            raise CustomException(e,sys)


