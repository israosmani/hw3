import logging
import os
from app import App
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access an environment variable (you can change 'MY_ENV_VARIABLE' to whatever you've set in the .env file)
env_var = os.getenv('MY_ENV_VARIABLE', 'No environment variable found')

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log output will go to app.log
    level=logging.INFO,  # Log INFO level and above
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    # Output the environment variable to the terminal
    print(f"Environment Variable Loaded: {env_var}")
    
    logging.info("Starting the application...")
    app = App().start()  # Your existing code to start the app
    logging.info("Application exited.")

