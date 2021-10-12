# exemplo de web scraping para leitura de dados de um site
# site a ser lido 'https://pt.stackoverflow.com/questions/tagged/python'
# libs: requests(pip install requests se na venv) / beatifulsoup4(pip install beautifulsoup4 se na venv)
import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print(data.text, titulo.text, votos.text, sep='\t')