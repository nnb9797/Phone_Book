

def string_counter():
    with open("phonebook.txt") as phonebook:
        last_used_id = 0
        for i in phonebook:
            last_used_id = i.split("**")[0]
    return last_used_id


def create_note():
    with open('phonebook.txt', 'r') as phonebook:
        temp = phonebook.readlines()[-1]
        # print(temp)
        new_id = int(temp.split("**")[0])
        # print(new_id)
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        comment = input("Введите комментарий: ")
    with open('phonebook.txt', 'a+') as phonebook:
        phonebook.write(f"\n{(new_id+1)}**{last_name}**{first_name}**{phone_number}**{comment}")
        print(f"\nЗапись внесена")


def delete_note():
    id_to_del = input("Введите id записи для удаления: ")
    temp = ""
    with open("phonebook.txt", "r") as phonebook:
        for i in phonebook:
            if i.split("**")[0] != id_to_del:
                temp += i
    with open("phonebook.txt", "w") as phonebook:
        phonebook.write(temp)
        print(f"\nЗапись удалена")
