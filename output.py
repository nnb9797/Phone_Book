def print_note(sep: str):
    check = 0
    id_to_print = input("Введите номер записи для вывода: ")
    with open("phonebook.txt") as phonebook:
        for i in phonebook:
            if i.split('**')[0] == id_to_print:
                print(sep.join(i.split("**")))
                check = 1
    if check == 0:
        print("Такой записи нет")


def print_phonebook(sep: str):
    with open("phonebook.txt") as phonebook:
        for i in phonebook:
            print((sep.join(i.split('**'))))
