### Project Demonstration / Demonstração do Projeto

![Project Demonstration / Demonstração do Projeto](https://github.com/arnesanches/beautiful-news-scraper/blob/main/Anima%C3%A7%C3%A3o.gif?raw=true)

#### English

# Beautiful News Scraper

This Python script collects data from Hacker News, generates a CSV report containing all the news and their respective votes, and creates a horizontal bar chart showing the top 10 most voted news items. The collected data can be used for trend analysis, news monitoring, identifying popular topics in the technology community, and other applications that require up-to-date information from Hacker News.

## Features

*   Collects the titles and votes of news from the Hacker News homepage.
*   Generates a complete report in CSV format, sorted by the number of votes (descending order).
*   Creates a horizontal bar chart displaying the top 10 most voted news items.
*   Saves the CSV report and the chart in a folder called `relatorios_hacker_news`.
*   Error handling to ensure the script's robustness.

## Prerequisites

Make sure you have Python installed on your system. You can download the latest version of Python from [https://www.python.org/downloads/](https://www.python.org/downloads/). In addition, the following Python libraries are required:

*   `requests`
*   `beautifulsoup4`
*   `pandas`
*   `matplotlib`

You can install them using `pip`:
```bash
pip install requests beautifulsoup4 pandas matplotlib
```
## How to use

1.  Clone this repository or download the `beautiful_news_scraper.py` script.
2.  Navigate to the directory where the script is located using the terminal or command prompt.
3.  Run the script with the command:

```bash
python beautiful_news_scraper.py
```
## Output

After execution, the script will create a folder called `relatorios_hacker_news` in the same directory. Inside this folder, you will find:

*   `hacker_news_report.csv`: A CSV file containing all the collected news and their respective votes, sorted from highest to lowest number of votes.
*   `hacker_news_top10_graph.png`: A PNG image containing the horizontal bar chart with the top 10 most voted news items.

The script will also print informative messages to the console during execution, indicating progress and the location where the files were saved.

## Code Structure

The code is divided into functions for better organization:

*   `fetch_hacker_news_data()`: Collects data from Hacker News using `requests` and `BeautifulSoup`. Returns a Pandas DataFrame.
*   `generate_report(dataframe)`: Generates the CSV report and the bar chart.
*   `if __name__ == "__main__":`: Main entry point of the script. Executes the main functions and handles potential errors.

## Notes

*   The script uses the `matplotlib` library to generate the chart, which displays the chart on the screen using the `plt.show()` command, in addition to saving the `.png` file. If you do not want the chart to be displayed on the screen, simply remove or comment out this line.
*   The script handles potential errors during the HTTP request and general execution, displaying informative messages in the console.
*   The chart size can be adjusted by modifying the parameters of the `plt.figure(figsize=(12, 8))` function.

## Contributions

Contributions are welcome! Feel free to open issues or pull requests in this repository.

## License

This project is licensed under the MIT License.

##
---

#### Português

# Beautiful News Scraper

Este script Python coleta dados do Hacker News, gera um relatório em formato CSV contendo todas as notícias e seus respectivos votos, e cria um gráfico de barras horizontal mostrando as 10 notícias mais votadas. Os dados coletados podem ser usados para análise de tendências, monitoramento de notícias, identificação de tópicos populares na comunidade de tecnologia, e outras aplicações que necessitam de informações atualizadas do Hacker News.

## Funcionalidades

*   Coleta os títulos e votos das notícias da página inicial do Hacker News.
*   Gera um relatório completo em formato CSV, ordenado por número de votos (ordem decrescente).
*   Cria um gráfico de barras horizontal exibindo as 10 notícias mais votadas.
*   Salva o relatório CSV e o gráfico em uma pasta chamada `relatorios_hacker_news`.
*   Tratamento de erros para garantir a robustez do script.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python em [https://www.python.org/downloads/](https://www.python.org/downloads/). Além disso, as seguintes bibliotecas Python são necessárias:

*   `requests`
*   `beautifulsoup4`
*   `pandas`
*   `matplotlib`

Você pode instalá-las usando o `pip`:
```bash
pip install requests beautifulsoup4 pandas matplotlib
```
## Como usar

1.  Clone este repositório ou baixe o script `beautiful_news_scraper.py`.
2.  Navegue até o diretório onde o script está localizado usando o terminal ou prompt de comando.
3.  Execute o script com o comando:
```bash
python beautiful_news_scraper.py
```
## Saída

Após a execução, o script criará uma pasta chamada `relatorios_hacker_news` no mesmo diretório. Dentro desta pasta, você encontrará:

*   `hacker_news_report.csv`: Um arquivo CSV contendo todas as notícias coletadas e seus respectivos votos, ordenados do maior para o menor número de votos.
*   `hacker_news_top10_graph.png`: Uma imagem PNG contendo o gráfico de barras horizontal com as 10 notícias mais votadas.

O script também imprimirá mensagens informativas no console durante a execução, indicando o progresso e o local onde os arquivos foram salvos.

## Estrutura do Código

O código está dividido em funções para melhor organização:

*   `fetch_hacker_news_data()`: Coleta os dados do Hacker News usando `requests` e `BeautifulSoup`. Retorna um DataFrame do Pandas.
*   `generate_report(dataframe)`: Gera o relatório CSV e o gráfico de barras.
*   `if __name__ == "__main__":`: Ponto de entrada principal do script. Executa as funções principais e trata possíveis erros.

## Observações

*   O script utiliza a biblioteca `matplotlib` para gerar o gráfico, que exibe o gráfico na tela através do comando `plt.show()`, além de salvar o arquivo `.png`. Caso você não queira que o gráfico seja exibido na tela, basta remover ou comentar essa linha.
*   O script trata possíveis erros durante a requisição HTTP e a execução geral, exibindo mensagens informativas no console.
*   O tamanho do gráfico pode ser ajustado modificando os parâmetros da função `plt.figure(figsize=(12, 8))`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests neste repositório.

## Licença

Este projeto está licenciado sob a MIT License.


