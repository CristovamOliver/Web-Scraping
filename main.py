from bs4 import BeautifulSoup
from requests import get

#Especificando URL
url = 'https://www.imdb.com/title/tt0903747/episodes?season=1'
#Obtendo os dados
response = get(url)
#Apresentando a estrutura geral da página
# print(response.text[:250])

html_soup = BeautifulSoup(response.text, 'html.parser')

# print(html_soup)

container = html_soup.find_all('div', class_='info')



temp_ep =  html_soup.find_all('h3')['episode_top']
nome_ep =  container[0].find('a')['title']
data_ep =  container[0].find('div', class_='airdate').text.strip()
nota_ep =  container[0].find('span', class_='ipl-rating-star__rating').text.strip()


print(f'Temporada: {temp_ep}')
# print(f'Nome do episódio: {nome_ep}')
# print(f'Data do episódio: {data_ep}')
# print(f'Nota do episódio: {nota_ep}')

