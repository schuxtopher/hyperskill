import requests

from bs4 import BeautifulSoup


def print_heading(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    h1 = soup.find('h1')

    print(h1.text)


print_heading(input())
