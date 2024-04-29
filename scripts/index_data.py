# index_data.py
from elasticsearch import Elasticsearch
import config.settings as cfg
import os

es = Elasticsearch([{'host': cfg.ELASTICSEARCH_HOST, 'port': cfg.ELASTICSEARCH_PORT}])

def index_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    response = es.index(index=cfg.ELASTICSEARCH_INDEX, document={'content': content})
    return response

def preprocess_and_index_files():
    exclude_patterns = ['node_modules', '.sln', '.csproj']
    for subdir, dirs, files in os.walk(cfg.CURRENT_REPO_PATH):
        for file in files:
            file_path = os.path.join(subdir, file)
            if not any(x in file_path for x in exclude_patterns):
                print(f"Indexing {file_path}")
                index_file(file_path)

def main():
    preprocess_and_index_files()

if __name__ == "__main__":
    main()
