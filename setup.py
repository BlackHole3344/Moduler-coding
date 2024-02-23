from setuptools import setup , find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "This is my machine learning moduler coding project"
AUTHOR_NAME = "Ganesh"
AUTHOR_EMAIL = "insideinsane17@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    with open (REQUIREMENTS_FILE_NAME) as requirment_file:
        requirment_list = requirment_file.readlines()
        requirment_list = [requirement_name.replace("\n" ,"") for requirement_name in requirment_list]
        if HYPHEN_E_DOT in requirment_list:
            requirment_list.remove(HYPHEN_E_DOT)
            
        return requirment_list


setup(name = PROJECT_NAME , 
      version= VERSION , 
      description= DESCRIPTION , 
      author=AUTHOR_NAME , 
      author_email=AUTHOR_EMAIL , 
      packages=find_packages() , 
      install_requires = get_requirements_list()
      )