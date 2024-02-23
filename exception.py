from flask import Flask 
from src.logger import logging
from src.exception import MyException
import os , sys 


app = Flask(__name__)

@app.route('/' , methods = ["GET" , "POST"])

def index():
    try :
        raise Exception("we are testing our exception file")
    except  Exception as e :
        ML = MyException(e , sys)
        logging.info(ML.error_message)
        logging.info("we are testing out logging file")
        return "welcome"

if __name__ == "__main__":
    app.run(debug = True)
    