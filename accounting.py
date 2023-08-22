def command_p_people(documents: list, doc_number: str) -> str:
    for x in documents:
        if doc_number in x.values():
            return x['name']
    else:
        return 'Вы ввели несуществующий документ.'


def command_s_shelf(directories: dict, doc_number: str) -> str:
    for x, y in directories.items():
        if doc_number in y:
            return f'Документ находится на плоке {x}'
    else:
        return 'Вы ввели несуществующий документ.'


def command_l_list(documents: list) -> str:
    list_for_return = [f'{list(x.values())[0]} "{list(x.values())[1]}" "{list(x.values())[2]}"' for x in documents]
    return list_for_return


def command_a_add(documents: list, directories: dict, doc_number: str, doc_type: str, name_in_doc: str, shell_number: str) -> str:
    if shell_number in directories:
        documents.append({"type": doc_type, "number": doc_number, "name": name_in_doc})
        directories[shell_number].append(doc_number)
        return 'Добавление выполнено успешно'
    else:
        return f'Полки {shell_number} не существует. Сначала создайте ее c помощью команды "as"'


def command_d_delete(documents: list, directories: dict, doc_number: str) -> str:
    for x, y in enumerate(documents):
        if doc_number in y.values():
            del(documents[x])
    for z, n in directories.items():
        if doc_number in n:
            n.remove(doc_number)
            return 'Удаление выполнено успешно.'
    else:
        return 'Неправильно указан номер документа.'


def command_m_move(directories: dict, doc_number: str, shell_number: str) -> str:
    for z, n in directories.items():
        if doc_number in n and shell_number in directories.keys():
            directories[shell_number].append(doc_number)
            n.remove(doc_number)
            return 'Перемещение выполнено.'
    else:
        return 'Неправильно указан номер документа или такой полки не существует.'


def command_as_add_shelf(directories: dict, new_shell_number: str) -> str:
    if new_shell_number not in directories.keys():
        empty_list = []
        directories[new_shell_number] = empty_list
        return 'Полка добавлена.'
    else:
        return 'Такая полка уже существует.'


if __name__ == '__main__':
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
    directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }

    print('Справка по командам:\n'
          'p - people;\n'
          's - shelf;\n'
          'l - list;\n'
          'a - add;\n'
          'd - delete;\n'
          'm - move;\n'
          'as - add shelf\n'
          'q - quit')

    while True:
        command = input('\nВведите команду: ')
        if command == 'p':
            doc_number = input('Введите номер документа: ')
            print(command_p_people(documents, doc_number))
        if command == 's':
            doc_number = input('Введите номер документа: ')
            print(command_s_shelf(directories, doc_number))
        if command == 'l':
            print(command_l_list(documents))
        if command == 'a':
            doc_number = input('Введите номер документа: ')
            doc_type = input('Введите тип документа: ')
            name_in_doc = input('Введите имя владельца: ')
            shell_number = input('Введите номер полки: ')
            print(command_a_add(documents, directories, doc_number, doc_type, name_in_doc, shell_number))
        if command == 'd':
            doc_number = input('Введите номер документа: ')
            print(command_d_delete(documents, directories, doc_number))
        if command == 'm':
            doc_number = input('Введите номер документа: ')
            shell_number = input('Введите номер полки: ')
            print(command_m_move(directories, doc_number, shell_number))
        if command == 'as':
            new_shell_number = input('Введите номер новой полки: ')
            print(command_as_add_shelf(directories, new_shell_number))
        if command == 'q':
            break
