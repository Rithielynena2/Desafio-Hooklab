import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.reddit.com/r/programming/top/.json?limit=3'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


response = requests.get(url, headers=headers)


if response.status_code == 200:
    data = response.json()

    titulos = []
    upvotes = []
    links = []

    for postagem in data['data']['children']:
        titulos.append(postagem['data']['title'])
        upvotes.append(postagem['data']['ups'])
        links.append('https://www.reddit.com' + postagem['data']['permalink'])

    df = pd.DataFrame({
        'Título': titulos,
        'Upvotes': upvotes,
        'Link': links
    })

    df.to_csv('programming_subreddit_top_posts.csv', index=False)

    print("Dados salvos em 'programming_subreddit_top_posts.csv'.")
else:
    print(f"Falha ao acessar o subreddit: {response.status_code}")
