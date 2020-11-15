import requests

from bs4 import BeautifulSoup


def get_translation(word, lang):
    translation_direction = {'en': 'french-english',
                             'fr': 'english-french'}
    base_url = 'https://context.reverso.net/translation'
    lang_url = '/' + translation_direction[lang]
    word_url = '/' + word
    url = base_url + lang_url + word_url
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get(url, headers=headers)

    if r.status_code:
        print(r.status_code, 'OK', '\n')

        soup = BeautifulSoup(r.content, 'html.parser')
        translation_content = soup.find(id="translations-content")
        examples_content = soup.find(id="examples-content")

        translations = translation_content.text.split()

        examples = examples_content.text.split('\n')
        # remove empty elements and strip unnecessary spaces from example sentences
        examples = list(map(str.strip, filter(None, examples)))

        lang_names = {'en': 'English',
                      'fr': 'French'}

        print("Context examples:", '\n')

        print(lang_names[lang] + " Translations:")
        print('\n'.join(translations[:5]), '\n')

        print(lang_names[lang] + " Examples:")
        for i, sentence in enumerate(examples[:10]):
            print(sentence)
            if i % 2:
                print()


def start():
    print('Type "en" if you want to translate from French into English,'
          ' or "fr" if you want to translate from English into French:')
    lang = input()
    word = input('Type the word you want to translate:\n')
    print(f'You chose "{lang}" as the language to translate "{word}"')
    get_translation(word, lang)


start()
