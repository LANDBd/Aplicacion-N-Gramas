from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

GH_TOKEN = os.getenv('GH_TOKEN')