import requests

from bs4 import BeautifulSoup


def print_nth_hyperlink(n, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    a = soup.find_all('a')

    print(a[n - 1].get('href'))


print_nth_hyperlink(int(input()), input())
