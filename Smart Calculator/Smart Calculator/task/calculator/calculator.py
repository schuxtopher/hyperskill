from collections import deque


class Calculator:
    COMMANDS = {'/help': "This program calculates stuff",
                '/exit': "bye!"}

    PRECEDENCE = {'+': 1, '-': 1,
                  '*': 2, '/': 2,
                  '^': 3,
                  '(': 0, ')': 0}

    OPERATORS = {'+': lambda y, x: x + y,
                 '-': lambda y, x: x - y,
                 '*': lambda y, x: x * y,
                 '/': lambda y, x: x / y,
                 '^': lambda y, x: x ** y}

    def __init__(self):
        self.variables = {}

    def start(self):
        while True:
            input_string = input()
            if input_string:
                if input_string.startswith('/'):
                    self.print_cmd(input_string)
                    if input_string == '/exit':
                        break
                elif '=' in input_string:
                    self.assign_var(input_string)
                else:
                    self.evaluate(input_string)

    def print_cmd(self, string):
        try:
            print(self.COMMANDS[string])
        except KeyError:
            print("Unknown command")

    def assign_var(self, string):
        pos_eq_symbol = string.find('=')
        identifier = string[:pos_eq_symbol].strip()
        assignment = string[pos_eq_symbol + 1:].strip()
        try:
            assert identifier.isalpha()
        except AssertionError:
            print("Invalid identifier")
        else:
            self.save_var_in_dict(identifier, assignment)

    def save_var_in_dict(self, identifier, assignment):
        try:
            assert '=' not in assignment
            if assignment.isalpha():
                self.variables[identifier] = self.variables[assignment]
            else:
                assert assignment.isnumeric()
                self.variables[identifier] = assignment
        except AssertionError:
            print("Invalid assignment")
        except KeyError:
            print("Unknown variable")

    def evaluate(self, string):
        """ Evaluates the term in given string and returns the result"""

        try:
            infix = self.string_to_infix(string)
            postfix = self.infix_to_postfix(infix)
            assert not any(x in postfix for x in ['(', ')'])
            result = self.postfix_to_result(postfix)
            print(result)
        except (AssertionError, IndexError):
            print('Invalid expression')
        except KeyError:
            print("Unknown variable")

    def string_to_infix(self, string):
        """ Conversion to infix notation"""

        term = list(string)

        term = self.merge_signs(term, '+')
        term = self.merge_signs(term, '-')
        term = self.merge_operands(term)
        term = self.merge_operands(term, alpha=True)
        term = self.remove_spaces(term)

        if term[0] == '-':
            term[1] = term[0] + term[1]
            term.popleft()
        elif term[0] == '+':
            term.popleft()

        return term

    @staticmethod
    def merge_signs(term, sign):
        """ Removes redundant signs"""
        new_term = deque()
        sign_count = 0

        for char in term:
            if char == sign:
                sign_count += 1
            else:
                if sign_count and sign_count % 2 != 0:
                    new_term.append(sign)
                    sign_count = 0
                if sign_count and (sign_count % 2 == 0 or sign == '+'):
                    new_term.append('+')
                    sign_count = 0

                new_term.append(char)

        return new_term

    @staticmethod
    def merge_operands(term, alpha=False):
        """ Merges single digits to numbers"""
        new_term = deque()
        operand = ''

        for char in term:
            if alpha and char.isalpha():
                operand += char
            elif not alpha and char.isnumeric():
                operand += char
            else:
                if operand:
                    new_term.append(operand)
                    operand = ''
                new_term.append(char)

        if operand:
            new_term.append(operand)

        return new_term

    @staticmethod
    def remove_spaces(term):
        """ Removes spaces from term"""
        new_term = deque()

        while term:
            if term[-1] == ' ':
                term.pop()
            else:
                new_term.appendleft(term.pop())

        return new_term

    def infix_to_postfix(self, infix):
        """ Converts infix term into a postfix term"""

        operands = deque()
        postfix = deque()

        for element in infix:
            if element.isalpha():
                postfix.append(self.variables[element])
            elif element.isnumeric() or len(element) > 1:
                postfix.append(element)
            else:

                if not operands or operands[-1] == '(':
                    operands.append(element)
                else:

                    if element == '(':
                        operands.append(element)
                    elif element == ')':

                        while operands[-1] != '(':
                            postfix.append(operands.pop())
                        operands.pop()

                    elif self.PRECEDENCE[element] > self.PRECEDENCE[operands[-1]]:
                        operands.append(element)
                    else:

                        while operands and self.PRECEDENCE[element] <= self.PRECEDENCE[operands[-1]]:
                            postfix.append(operands.pop())
                        operands.append(element)

        while operands:
            postfix.append(operands.pop())

        return postfix

    def postfix_to_result(self, postfix):
        """ Calculates the result of a term in postfix notation"""

        result = deque()

        for element in postfix:
            if element.isnumeric():
                result.append(element)
            elif len(element) > 1:
                result.append(int(element))
            elif element in self.OPERATORS:
                result.append(self.OPERATORS[element](int(result.pop()), int(result.pop())))

        return result.pop()


if __name__ == "__main__":
    calc = Calculator()
    calc.start()
