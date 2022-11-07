# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import html5lib
import pandas as pd
from bs4 import BeautifulSoup


def main():
    testate = pd.read_csv(r'C:\Users\joned\OneDrive\Desktop\NBASTATS\players.csv')
    names = testate['Player'].values.tolist()
    for name in names:
        holder = name.split()
        firstname = holder[0]
        lastname = holder[1]
        if len(lastname) > 5:
            lastname = lastname[0:5]
        firstname = lastname + firstname[0:2]
        url_test = 'https://www.basketball-reference.com/players/{}/{}01/gamelog/2023'
        url = url_test.format(firstname[0], firstname)
        data = requests.get(url)

        with open('player{}.html'.format(firstname), 'w', encoding = 'utf-8') as f:
            f.write(data.text)
        page = open('player{}.html'.format(firstname), encoding = 'utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        regular_season = soup.find(id = 'pgl_basic')
        player_season = pd.read_html(str(regular_season))
    print('end')

