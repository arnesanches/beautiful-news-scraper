import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# Configuração da URL base
URL = "https://news.ycombinator.com/"

# Função para coletar dados do Hacker News
def fetch_hacker_news_data():
    # Faz uma requisição à página inicial do Hacker News
    response = requests.get(URL)
    response.raise_for_status()  # Lança um erro se a requisição falhar
    
    # Analisa o HTML da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extração dos títulos das notícias
    titles = [title.get_text() for title in soup.select('.titleline > a')]
    
    # Extração dos votos das notícias
    scores = [score.get_text() for score in soup.select('.score')]
    
    # Remove o texto "points" e converte para números inteiros
    scores = [int(score.split()[0]) for score in scores]
    
    # Garante que a quantidade de títulos e votos esteja alinhada
    if len(titles) > len(scores):
        titles = titles[:len(scores)]
    
    # Retorna os dados em um DataFrame do Pandas
    return pd.DataFrame({'Título': titles, 'Votos': scores})