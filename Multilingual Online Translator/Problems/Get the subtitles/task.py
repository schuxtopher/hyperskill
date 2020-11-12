import requests

from bs4 import BeautifulSoup


def print_nth_subtitle(n, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    h2 = soup.find_all('h2')

    print(h2[n].text)


print_nth_subtitle(int(input()), input())
