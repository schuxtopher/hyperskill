import requests

from bs4 import BeautifulSoup


def get_translation(word, lang):
    base_url = 'https://context.reverso.net/translation'
    lang_url = lang_to_url(lang)
    word_url = '/' + word
    url = base_url + lang_url + word_url
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get(url, headers=headers)

    if r.status_code:
        print(r.status_code, 'OK')

    soup = BeautifulSoup(r.content, 'html.parser')
    translation = soup.find(id='translations-content')
    examples = soup.find(id='examples-content')

    print("Translations")
    print([word for word in translation.text.split()])
    print([word for word in examples.text.split()])


def lang_to_url(lang):
    if lang == 'en':
        return '/french-english'
    elif lang == 'fr':
        return '/english-french'


def start():
    print('Type "en" if you want to translate from French into English,'
          ' or "fr" if you want to translate from English into French:')
    lang = input()
    word = input('Type the word you want to translate:\n')
    print(f'You chose "{lang}" as the language to translate "{word}"')
    get_translation(word, lang)


start()
