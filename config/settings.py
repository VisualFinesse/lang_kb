# config/settings.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'localhost')
ELASTICSEARCH_PORT = int(os.getenv('ELASTICSEARCH_PORT', 9200))
ELASTICSEARCH_INDEX = os.getenv('ELASTICSEARCH_INDEX', 'knowledge_base')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CURRENT_REPO_PATH = os.getenv('CURRENT_REPO_PATH', '/path/to/default/repository')
