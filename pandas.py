#!/usr/bin/python3

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/robinske/password-data/master/passwords/part-00000-abca9f4b-5795-47ee-8382-f523480a532f.csv',
)

import requests
r = requests.get('https://github.com/robinske/password-data/tree/master/passwords')
#print(r.status_code)

#print(r.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
all_links = soup.findAll('a', class_='js-navigation-open Link--primary')
data_links = [
    'https://raw.githubusercontent.com' + x.get('href').replace('blob/', '')
    for x in all_links
]


from tqdm import tqdm
all_dfs = [pd.read_csv(link) for link in tqdm(data_links[:10])]

passwords_df = pd.concat(all_dfs, ignore_index=True)

passwords_df.to_csv('data/test.csv', index=False)