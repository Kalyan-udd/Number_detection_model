import logging
import sys
import os

logger = logging.getLogger("Number_prediction")
logger.setLevel(logging.INFO)
if not logger.handlers:
    
    # Optional: Create a 'logs' directory if it doesn't exist to keep things clean
    os.makedirs("logs", exist_ok=True)
    
    # 2. Create a handler to write logs to a file
    file_handler = logging.FileHandler("logs/app.log", mode="a")
    file_handler.setLevel(logging.INFO)

    # 3. Create a handler to display logs on the screen/console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # 4. Define the layout/format of the log messages
    # This uses the updated format with filename and line number!
    log_formatter = logging.Formatter(
        "%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s", 
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Attach the format to both handlers
    file_handler.setFormatter(log_formatter)
    console_handler.setFormatter(log_formatter)

    # 5. Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)