import os

from dotenv import load_dotenv

load_dotenv()

postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')

CONNECTION_STRING="postgresql://{}:{}@{}:{}/llm-slack-bot".format(postgres_user, postgres_password, postgres_host, postgres_port)
COLLECTION_NAME='llm-slack-bot-play'

