import os
import logging
from pathlib import Path
import sys

project_name = "Number_recognition_model"

os.makedirs("logs", exist_ok=True)
logger_filepath = os.path.join("logs", "template.log")

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s]: %(filename)s - %(message)s',
                    handlers=[
                        logging.FileHandler(logger_filepath),
                        logging.StreamHandler(sys.stdout)]
                        )

list_of_files = [
    "src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logger.py",
    "requirements.txt",
    "logs/.gitkeep",
    "model_training/__init__.py",
    "model_training/model.py",
    "setup.py",
    "Dockerfile",
    ".dockerignore",
    "templates/home.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"making directory {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"making file {filepath}")

    else:
        logging.info(f"file already exist {filepath}")
        
    