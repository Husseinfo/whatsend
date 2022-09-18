from tkinter import Tk
from tkinter import filedialog

from main import start

MAX_SLEEP_BETWEEN_MESSAGES = 10


def file_picker():
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select WhatsApp spreadsheet",
                                               filetypes=(("Excel", "*.xls"), ("Excel", "*.xlsx")))
    return root.filename


def main():
    file_name = file_picker()
    if not file_name:
        exit(-1)
    start(file_name)


if __name__ == '__main__':
    main()
