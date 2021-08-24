import requests
import pickle
import os
import json
from bs4 import BeautifulSoup as BS
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'

response = requests.get(url)

resultado = BS(response.content, 'html5lib')

links_a = resultado.find_all('a', href=True)

links_http = [l.get('href') for l in links_a if 'http' in l.get('href')]

links_zip = [elem for elem in links_http if elem.find('.zip') != -1 and elem.find('grant_full_text') != -1]

my_dict = defaultdict(list)

for ano in range(1976, 2016):
    for link in links_zip:
        if link.find(str(ano)) != -1:
            my_dict[ano].append(link)

x_bar = []
y_bar = []
# imprime cada ano e a sua quantidade de links correspondente. As variáveis serão usadas posteriormente para imprimir um gráfico de barras
for key, value in my_dict.items():
    x_bar.append(key)
    y_bar.append(len([item for item in value if item]))
    print(key, len([item for item in value if item]))

if not os.path.exists('data'):
    os.mkdir('data')


# função que salva um arquivo picle
def save_pickle(ob, name='data/my_pickle'):
    with open(name, 'wb') as handler:
        pickle.dump(ob, handler)
    print('Pickle Saved!!!')


save_pickle(my_dict)


# função que salva um arquivo json
def save_json(ob, name='data/dict_to_json'):
    with open(name, 'w') as outfile:  # usar 'w' ou 'wb'?
        json.dump(ob, outfile)
    print('Json saved!!!')


save_json(my_dict)

# imprimindo gráfico de barras com o resultado 
plt.bar(x_bar, y_bar)
plt.show()