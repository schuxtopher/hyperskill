import requests
import sys

from bs4 import BeautifulSoup


class Translator:
    def __init__(self, source, target, word):
        self.search_url = 'https://context.reverso.net/translation'
        self.languages = ['Arabic', 'German', 'English', 'Spanish', 'French',
                          'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
                          'Romanian', 'Russian', 'Turkish']
        self.src = source
        self.trg = target
        self.wrd = word
        self.start()

    def start(self):
        if self.src.capitalize() not in self.languages:
            print(f"Sorry, the program doesn't support {self.src}")
            return

        if self.trg.capitalize() not in self.languages + ['All']:
            print(f"Sorry, the program doesn't support {self.trg}")
            return

        try:
            if self.trg == 'all':
                self.get_all_translations()
                with open(f"{self.wrd}.txt", 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                translations, examples = self.get_translation(self.trg)
                self.print_translation(self.trg, translations, examples)
        except ConnectionError:
            print("Something wrong with your internet connection")
        except AttributeError:
            print(f"Sorry, unable to find {self.wrd}")

    def menu(self):
        print("Hello, you're welcome to the translator. Translator supports:")
        for i, lang in enumerate(self.languages):
            print(f"{i + 1}. {lang}")

        print("Type the number of your language:")
        self.src = self.languages[int(input()) - 1]

        print("Type the number of language you want to translate to "
              "or '0' to translate to all languages:")
        if trg := int(input()):
            self.trg = self.languages[trg - 1]
        else:
            self.trg = 'all'

        print("Type the word your want to translate:")
        self.wrd = input()
        print()

        if self.trg == 'all':
            self.get_all_translations()
            with open(f"{self.wrd}.txt", 'r', encoding='utf-8') as f:
                print(f.read())
        else:
            translations, examples = self.get_translation()
            self.print_translation(trg, translations, examples)

    def get_translation(self, target):
        url = f"{self.search_url}/{self.src.lower()}-{target.lower()}/{self.wrd}"
        headers = {'user-agent': 'my-app/0.0.1'}

        r = requests.get(url, headers=headers)

        if r.status_code:
            # print(request.status_code, 'OK', '\n')
            translations, examples = self.mine_translation(r)
            return translations, examples

    def get_all_translations(self):
        with open(f'{self.wrd}.txt', 'w', encoding='utf-8') as f:
            for lang in self.languages:
                if lang.lower() == self.src.lower():
                    continue
                translations, examples = self.get_translation(lang)

                print(lang + " Translations:", file=f)
                print(translations[0], '\n', file=f)
                print(lang + " Example:", file=f)
                print(f"{examples[0]}:", file=f)
                print(f"{examples[1]}", '\n', file=f)

    @staticmethod
    def mine_translation(request):
        soup = BeautifulSoup(request.content, 'html.parser')
        translation_content = soup.find(id="translations-content")
        examples_content = soup.find(id="examples-content")

        translations = translation_content.text.split()

        examples = examples_content.text.split('\n')
        # remove empty elements and strip unnecessary spaces from example sentences
        examples = list(map(str.strip, filter(None, examples)))

        return translations, examples

    @staticmethod
    def print_translation(language, translations, examples):
        print(language + " Translations:")
        print('\n'.join(translations[:5]), '\n')

        print(language + " Examples:")
        for i, sentence in enumerate(examples[:10]):
            print(sentence)
            if i % 2:
                print()


if __name__ == '__main__':
    args = sys.argv
    print(args)
    translator = Translator(args[1], args[2], args[3])
