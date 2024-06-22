import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    conn = sqlite3.connect('tweets.db')
    df = pd.read_sql_query("SELECT * FROM tweets", conn)

    # Exemplo de gráfico de barras dos tweets por usuário
    user_counts = df['user'].value_counts()
    user_counts.plot(kind='bar')
    plt.xlabel('User')
    plt.ylabel('Number of Tweets')
    plt.title('Number of Tweets by User')
    plt.show()
    conn.close()
