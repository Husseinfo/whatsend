from random import randint
from time import sleep

from excel_parser import get_rows
from web import init, send_message

MAX_SLEEP_BETWEEN_MESSAGES = 10


def start(file_name):
    report = {True: [], False: []}
    init()
    for number, text in get_rows(file_name):
        report[send_message(number, text)].append(number)
        sleep(randint(1, MAX_SLEEP_BETWEEN_MESSAGES))
    with open(file_name + '.success.txt', 'a') as f:
        for x in report[True]:
            f.write(f'{x}\n')

    with open(file_name + '.fail.txt', 'a') as f:
        for x in report[False]:
            f.write(f'{x}\n')


if __name__ == '__main__':
    start('/home/hsr/Documents/whatsapp.xlsx')
