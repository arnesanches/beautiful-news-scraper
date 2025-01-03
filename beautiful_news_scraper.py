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

# Função para gerar relatório e gráfico
def generate_report(dataframe):
    # Cria uma pasta chamada "relatorios_hacker_news" (se não existir)
    folder_name = "relatorios_hacker_news"
    os.makedirs(folder_name, exist_ok=True)
    
    # Ordena os dados por número de votos em ordem decrescente
    sorted_data = dataframe.sort_values(by='Votos', ascending=False)
    
    # Seleciona apenas o Top 10 das notícias mais votadas
    top_10_data = sorted_data.head(10)
    
    # Salva o relatório completo em formato CSV dentro da pasta criada
    csv_path = os.path.join(folder_name, 'hacker_news_report.csv')
    sorted_data.to_csv(csv_path, index=False)  # Salva sem os índices numéricos do DataFrame
    print(f"Relatório salvo como {csv_path}.")
    
    # Cria um gráfico de barras horizontal com as 10 notícias mais votadas
    plt.figure(figsize=(12, 8))  # Define o tamanho do gráfico
    plt.barh(top_10_data['Título'], top_10_data['Votos'], color='skyblue')  # Gera o gráfico
    plt.xlabel('Votos')  # Rótulo do eixo X
    plt.ylabel('Títulos')  # Rótulo do eixo Y
    plt.title('Top 10 Notícias do Hacker News por Votos')  # Título do gráfico
    plt.gca().invert_yaxis()  # Inverte a ordem do eixo Y para o maior valor ficar no topo
    plt.tight_layout()  # Ajusta automaticamente o layout para evitar cortes nos textos
    
    # Salva o gráfico como uma imagem dentro da pasta criada
    graph_path = os.path.join(folder_name, 'hacker_news_top10_graph.png')
    plt.savefig(graph_path, dpi=300)  # Salva a imagem com alta resolução
    print(f"Gráfico salvo como {graph_path}.")
    plt.show()  # Exibe o gráfico na tela

# Ponto de entrada principal do script
if __name__ == "__main__":
    try:
        print("Coletando dados do Hacker News...")
        # Coleta os dados do Hacker News
        data = fetch_hacker_news_data()
        print("Dados coletados com sucesso!")
        
        print("Gerando relatório e gráfico...")
        # Gera o relatório e o gráfico
        generate_report(data)
        print("Processo concluído!")
    except Exception as e:
        # Exibe uma mensagem de erro, caso algo dê errado
        print(f"Erro ao executar o script: {e}")