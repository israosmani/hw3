import os
import logging
from app import App


logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    handlers=[
        logging.FileHandler("app.log"),  
        logging.StreamHandler()  
    ]
)

def output_env_variables():
    environment = os.getenv('ENVIRONMENT')
    db_user = os.getenv('DATABASE_USERNAME')
    db_password = os.getenv('DATABASE_PASSWORD')
    logging_level = os.getenv('LOGGING_LEVEL')
    my_env_variable = os.getenv('MY_ENV_VARIABLE')

    logging.info(f"Environment: {environment}")
    logging.info(f"Database Username: {db_user}")
    logging.info(f"Database Password: {db_password}")  
    logging.info(f"Logging Level: {logging_level}")
    logging.info(f"My Environment Variable: {my_env_variable}")

if __name__ == "__main__":
    logging.info("Starting the app...")
    
    app = App().start()
    
    output_env_variables()
    
    logging.info("App finished execution.")

