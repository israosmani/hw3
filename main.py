import logging
import os
from app import App
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log output will go to app.log
    level=logging.INFO,  # Log INFO level and above
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Starting the application...")
    app = App().start()  # Your existing code to start the app
    logging.info("Application exited.")
