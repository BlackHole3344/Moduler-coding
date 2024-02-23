import logging 
import os , sys 
from datetime import datetime 

LOG_DIR = "logs"
LoG_DIR = os.path.join(os.getcwd() , LOG_DIR)

os.makedirs(LOG_DIR , exist_ok=True)

# describing the extensions of the files which will be created in logs
# .log
# saving logs files with current date time 
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log{CURRENT_TIME_STAMP}.log"
# output log_2024_-6_4_5.log
log_file_path = os.path.join(LOG_DIR , file_name)

logging.basicConfig(filename=log_file_path , 
                    filemode="w" , 
                    format= ' [%(asctime)s] %(name)s - %(levelname)s - %(message)s' ,level=logging.INFO)
