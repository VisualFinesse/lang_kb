# Large Repository Knowledge Base

## Overview
This project is designed to index a large repository into Elasticsearch and provide a querying interface using Langchain and OpenAI's API.

This setup ensures that your knowledge base system is modular, allowing easy switching between different repositories by adjusting the CURRENT_REPO_PATH in the settings. It also supports robust querying capabilities using advanced NLP models from OpenAI integrated with Elasticsearch.

## Prerequisites
- Python 3.x
- Elasticsearch
- OpenAI API key

## Setup
1. Clone this repository.
2. Install the required Python dependencies:

pip install -r requirements.txt

3. Configure your OpenAI API key and Elasticsearch settings in `config/settings.py`.

## Usage
- **Preprocessing and Indexing**: Run the preprocessing and indexing script to prepare and index the repository data into Elasticsearch.

python scripts/index_data.py

- **Querying**: To query the knowledge base, use the query script.

python scripts/query_kb.py

## Configuration
- Adjust the `CURRENT_REPO_PATH` in `config/settings.py` to point to the repository you wish to index.
- Configure Elasticsearch host and port in `config/settings.py`.

## Contributing
Contributions to improve this project are welcome. Please ensure that you update tests as appropriate.
