import logging, os
from datetime import datetime

LOG_FILE = "{datetime.now().strftime('%M_%D_%Y_%H_%M_%S')}.log"
log_path =os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s ', datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO,
)