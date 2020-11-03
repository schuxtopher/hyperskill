def solve():
    if hidden_operation('random') == 'random':
        print('or')
        print(hidden_operation(''))
    elif hidden_operation('') == '':
        print('and')
        print(hidden_operation('random'))
    elif hidden_operation(False):
        print('not')
