from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

import sys
if sys.platform.startswith("win"):
    import _locale
    # pylint: disable=protected-access
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if 'bonjour' not in reply or 'examples' not in reply.lower():
            return CheckResult.wrong("Looks like your program didn't print translations, examples or titles for them.\n"
                                     "Remember that your program should output lines \"... Translations\" and \"... Examples\",\n"
                                     "where ... is the name of the language.")
        reply = reply.lower().strip()
        bonjour_index = reply.index('bonjour')
        if 'examples' not in reply[bonjour_index:]:
            return CheckResult.wrong("Context examples should follow translations.\n"
                                     "It looks like in your program they go in the opposite order.")
        example_index = reply[bonjour_index:].index('examples') + bonjour_index
        translations_slice = reply[bonjour_index:example_index]
        if len(translations_slice.split('\n')) < 4:
            return CheckResult.wrong("Seems like your program did not place each translation on a new line.")
        if ("'" in translations_slice
            or ',' in translations_slice):
            return CheckResult.wrong("Seems like you didn't remove commas and quotation marks from translations.")
        if len(reply[example_index:].split('\n')) < 3:
            return CheckResult.wrong("Seems like your program did not place each example on a new line.")

        return CheckResult.correct()


if __name__ == '__main__':
    TranslatorTest('translator.translator').run_tests()
