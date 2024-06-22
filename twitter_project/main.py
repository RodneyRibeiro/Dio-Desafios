import os
from app.twitter_client import authenticate, fetch_tweets
from app.data_manager import create_table, insert_tweet
from app.report_generator import generate_report


def main():
    # Autenticação
    api = authenticate()

    # Criar tabela no banco de dados
    create_table()

    # Buscar tweets
    query = "#Python"
    tweets = fetch_tweets(api, query, count=100)

    # Inserir tweets no banco de dados
    for tweet in tweets:
        insert_tweet(tweet)

    # Gerar relatório
    generate_report()


if __name__ == "__main__":
    main()
