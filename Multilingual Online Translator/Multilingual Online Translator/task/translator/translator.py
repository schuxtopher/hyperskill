import requests

from bs4 import BeautifulSoup


def menu():
    languages = ['Arabic', 'German', 'English', 'Spanish', 'French',
                 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
                 'Romanian', 'Russian', 'Turkish']

    print("Hello, you're welcome to the translator. Translator supports:")
    for i, lang in enumerate(languages):
        print(f"{i + 1}. {lang}")

    print("Type the number of your language:")
    src = languages[int(input()) - 1]
    print("Type the number of language you want to translate to:")
    trg = languages[int(input()) - 1]
    print("Type the word your want to translate:")
    wrd = input()
    print()

    r = request_translation(src.lower(), trg.lower(), wrd)

    if r.status_code:
        # print(request.status_code, 'OK', '\n')
        translations, examples = mine_translation(r)
        print_translation(trg, translations, examples)


def request_translation(source, target, word):
    base_url = 'https://context.reverso.net/translation'
    lang_url = '/' + source + '-' + target
    word_url = '/' + word
    url = base_url + lang_url + word_url

    headers = {'user-agent': 'my-app/0.0.1'}

    return requests.get(url, headers=headers)


def mine_translation(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    translation_content = soup.find(id="translations-content")
    examples_content = soup.find(id="examples-content")

    translations = translation_content.text.split()

    examples = examples_content.text.split('\n')
    # remove empty elements and strip unnecessary spaces from example sentences
    examples = list(map(str.strip, filter(None, examples)))

    return translations, examples


def print_translation(language, translations, examples):
    print(language + " Translations:")
    print('\n'.join(translations[:5]), '\n')

    print(language + " Examples:")
    for i, sentence in enumerate(examples[:10]):
        print(sentence)
        if i % 2:
            print()


if __name__ == '__main__':
    menu()
