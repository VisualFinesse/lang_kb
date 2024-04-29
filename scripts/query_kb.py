# query_kb.py
from langchain.chains import SearchThenGenerateChain
from langchain.clients import OpenAIClient, ElasticsearchClient
import config.settings as cfg

# Initialize clients
es_client = ElasticsearchClient(hosts=[{'host': cfg.ELASTICSEARCH_HOST}])
openai_client = OpenAIClient(api_key=cfg.OPENAI_API_KEY)

# Set up the search-then-generate chain
chain = SearchThenGenerateChain(search_client=es_client, generate_client=openai_client)

def query_knowledge_base(question):
    response = chain.ask(question)
    return response

def main():
    question = input("Enter your query: ")
    response = query_knowledge_base(question)
    print(response)

if __name__ == "__main__":
    main()