import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from src.ML_project.expection import CustomException
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.ML_project.logger import logging

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class Data_Transformation:
    def __init__(self):
        self.data_transformationconfig = DataTransformationConfig()

    def get_data_transformer_obj(self):
        '''this func is responsible for data transformation'''

        try:
        
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(steps=[(
                "imputer", SimpleImputer(strategy="median")),
                ("Scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("Imputer", SimpleImputer(strategy="most_frequent")),
                ("OneHotEncoder", OneHotEncoder()),
                "Scaler", StandardScaler(with_mean=False)
            ])

            logging.info(f"Categorical Columns: {categorical_columns}")
            logging.info(f"Numerical Columns: {numerical_columns}")


            #Combines transformations for numeric and categorical data.
            preprocessor = ColumnTransformer(
                [
                    ("Num Pipeline", num_pipeline, numerical_columns),
                    ("Cat Pipeline", cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading the train and test file.")

            preprocessing_obj = self.get_data_transformer_obj()
            
            target_col = "math_score"
            num_col = ["Writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_col], axis=1)
            targert_feature_train_df = train_df[target_col]

            input_feature_test_df = test_df.drop(columns=[target_col], axis=1)
            targert_feature_test_df = test_df[target_col]



        except Exception as e:
            raise CustomException(sys, e)
                
        