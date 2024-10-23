import os
import logging
from app import App

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Use DEBUG, INFO, WARNING, etc., as needed
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.FileHandler("app.log"),  # Save logs to a file
        logging.StreamHandler()  # Also output logs to the terminal
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
    logging.info(f"Database Password: {db_password}")  # Be cautious logging sensitive data!
    logging.info(f"Logging Level: {logging_level}")
    logging.info(f"My Environment Variable: {my_env_variable}")

if __name__ == "__main__":
    # Log that the app is starting
    logging.info("Starting the app...")
    
    # Start the app
    app = App().start()
    
    # Output and log environment variables
    output_env_variables()
    
    # Log that the app finished execution
    logging.info("App finished execution.")

