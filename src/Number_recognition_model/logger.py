import logging
import sys

logger = logging.getLogger("Number_recogniser")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("logs/app.log", mode="a") 
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    log_formatter = logging.Formatter("[%(asctime)s - {%(pathname)s - %(lineno)d}] - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    
    file_handler.setFormatter(log_formatter)
    console_handler.setFormatter(log_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

print("logger has been created")