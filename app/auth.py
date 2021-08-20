# Authorizes the application to access the Spotify API
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

