import math
import sys


def calc_wrapper(**kwargs):
    if len(kwargs) < 4 \
            or 'type' not in kwargs \
            or 'interest' not in kwargs:

        print_error()
        return

    credit_type = kwargs['type']

    if credit_type == 'diff':
        diff_wrapper(**kwargs)
    elif credit_type == 'annuity':
        annuity_wrapper(**kwargs)
    else:
        print_error()
        return


def diff_wrapper(**kwargs):
    if 'payment' in kwargs:
        print_error()
        return

    interest = float(kwargs['interest']) / 1200
    periods = int(kwargs['periods'])
    principal = int(kwargs['principal'])

    payments = [mth_diff_payment(principal, interest, periods, period)
                for period in range(1, periods + 1)]

    for month, payment in enumerate(payments):
        print(f"Month {month + 1}: payment is {payment}")

    print(f"\nOverpayment = {sum(payments) - principal}")


def annuity_wrapper(**kwargs):

    if 'principal' not in kwargs:
        interest = float(kwargs['interest']) / 1200
        payment = int(kwargs['payment'])
        periods = int(kwargs['periods'])

        principal = loan_principal(payment, interest, periods)
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {payment * periods - principal}")

    if 'periods' not in kwargs:
        interest = float(kwargs['interest'])/ 1200
        payment = int(kwargs['payment'])
        principal = int(kwargs['principal'])

        periods = num_payments(payment, interest, principal)
        print(f"It will take {periods // 12} years to repay this loan!")
        print(f"Overpayment = {payment * periods - principal}")

    if 'payment' not in kwargs:
        interest = float(kwargs['interest']) / 1200
        periods = int(kwargs['periods'])
        principal = int(kwargs['principal'])

        payment = annuity_payment(principal, interest, periods)
        print(f"Your annuity payment = {payment}!")
        print(f"Overpayment = {payment * periods - principal}")


def create_arg_dic(args):
    clean_args = [args[i].lstrip('--').split('=') for i in range(1, len(args))]

    if all(map(lambda x: float(x) >= 0, [arg[1] for arg in clean_args[1:]])):
        return {key: value for (key, value) in clean_args}
    else:
        print_error()
        return {}


def mth_diff_payment(p, i, n, m):
    return int(math.ceil(p / n + i * (p - p * (m - 1) / n)))


def annuity_payment(p, i, n):
    return math.ceil(p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))


def loan_principal(a, i, n):
    return int(math.floor(a / (i * math.pow((1 + i), n) / (math.pow(1 + i, n) - 1))))


def num_payments(a, i, p):
    return math.ceil(math.log(a / (a - i * p), 1 + i))


def print_error():
    print("Incorrect parameters")


args = sys.argv

try:

    if arc_dic := create_arg_dic(args):
        calc_wrapper(**arc_dic)
except (KeyError, AssertionError, ValueError):
    print("Incorrect parameters")
