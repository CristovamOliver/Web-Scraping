from bs4 import BeautifulSoup
from requests import get


url = 'https://www.imdb.com/title/tt0903747/episodes?season=1'

response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')

container = soup.find_all('div', class_='info')

temp_ep =  soup.find_all('h3')[1].text.strip()
nome_ep =  container[0].find('a')['title']
data_ep =  container[0].find('div', class_='airdate').text.strip()
nota_ep =  container[0].find('span', class_='ipl-rating-star__rating').text.strip()

print(f'Temporada: {temp_ep}')
print(f'Nome do episódio: {nome_ep}')
print(f'Data do episódio: {data_ep}')
print(f'Nota do episódio: {nota_ep}') 