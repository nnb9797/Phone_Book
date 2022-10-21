import file_writing
import output



def menu():
    print("Меню справочника:\n"
          "1. Добавить запись\n"
          "2. Удалить запись\n"
          "3. Вывести запись по номеру\n"
          "4. Вывести весь справочник\n")
    point = 0
    while point < 1 or point > 4:
        point = int(input("Введите номер нужной операции: "))
        print()
    if point == 1:
        file_writing.create_note()
    if point == 2:
        file_writing.delete_note()
    if point == 3:
        output.print_note(', ')
    if point == 4:
        output.print_phonebook(', ')
    whaiting = input()