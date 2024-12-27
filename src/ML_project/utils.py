import os, sys
from src.ML_project.expection import CustomException
from src.ML_project.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
#thie will load all details from .env file
load_dotenv()

host = os.getenv("host")
user = os.getenv("username")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("reading sql database started")

    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection Established: {mydb}")
        df=pd.read_sql_query("select * from raw", mydb)
        print(df.head())

        return df
    except Exception as ex:
        raise CustomException(ex)


