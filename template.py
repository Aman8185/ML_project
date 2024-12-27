import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "ML_project"

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Components/data_ingestion.py",
    f"src/{project_name}/Components/Data_transformation.py",
    f"src/{project_name}/Components/model_trainer.py",
    f"src/{project_name}/Components/Data_monitering.py",
    f"src/{project_name}/pipelines/init.py",
    f"src/{project_name}/pipelines/training_pipelin.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/expection.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/expection.py",
    "app.py",
    "Docker.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info('Creating Directory:{filedir} for the file {filename}')

        if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath,'w') as f:
                pass
                logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filename} is already exists")