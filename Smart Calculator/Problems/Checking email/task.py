def check_email(string):
    return all([' ' not in string,
                string.count('@') == 1,
                string[string.find('@') + 1] != '.',
                '.' in string[string.find('@') + 2:]])
