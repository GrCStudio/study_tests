documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def secretary_people(inp_num):
    for doc in documents:
        if doc["number"] == inp_num:
            print(doc["name"])
            return doc["name"]
    doc_counter = 0
    for doc in documents:
        if doc["number"] != inp_num:
            doc_counter += 1
    if doc_counter == len(documents):
        print("Нет такого документа!")
        return False

def secretary_shelf(inp_num):
    for dir in directories:
        doc_counter = 0
        if inp_num not in directories[dir]:
            doc_counter += 1
    if doc_counter == len(directories):
        print("Нет такого документа!")
        return False
    for dir in directories:
        if inp_num in directories[dir]:
            # print ("Полка: ", dir)
            return dir

def secretary_list():
    for doc in documents:
        print(doc["type"], doc["number"], doc["name"])
        return (doc["type"], doc["number"], doc["name"])

def secretary_add(doc_type,doc_number,doc_name,dic_number):
    while True:

        if dic_number in directories:
            break
        else:
            print("Нет такой полки.")
            return False
    newdoc = {"type": doc_type, "number": doc_number, "name": doc_name}
    documents.append(newdoc)
    directories[dic_number].append(doc_number)
    return newdoc

def secretary_delete(inp_num):
    doc_counter = 0
    for doc in documents:
        if doc["number"] != inp_num:
            doc_counter += 1
    if doc_counter == len(documents):
        print("Нет такого документа!")
        return False
    list_counter = 0
    for doc in documents:
        if doc["number"] == inp_num:
            del documents[list_counter]
            return True
        list_counter += 1
    secretary_delete_from_shelf(inp_num)

def secretary_delete_from_shelf(inp_num):
    dir = secretary_shelf(inp_num)
    dir_counter = 0
    for docs in directories[dir]:
        if docs == inp_num:
            del directories[dir][dir_counter]
            return True
        dir_counter += 1

def secretary_move(inp_num, shelf):
    check = secretary_shelf(inp_num)
    if check is None:
        print("Нет такой полки!")
        return False
    else:
        secretary_delete_from_shelf(inp_num)
        directories[shelf].append(inp_num)
        return directories[shelf]

def secretary_add_shelf(inp_num):
    if inp_num in directories:
        print("Есть такая полка.")
        return True
    else:
        directories[inp_num] = []
        return directories[inp_num]


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print("\nРабочее место секретаря. Введите команду. '?' или 'help' для справки.")
        work_input = input()
        if work_input == 'help' or work_input == '?':
            print("""Список поддерживаемых действий:\n
        ?, help - эта справка;\n
        p, people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n
        s, shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n
        l, list – команда, которая выведет список всех документов;\n
        a,  add – команда, которая добавит новый документ в каталог и в перечень полок;\n
        d,  delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;\n
        m, move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
        as, add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
        e, exit – выход.
        """)
        elif work_input == 'p' or work_input == 'people':
            doc_number = input("Введите номер документа:\n")
            secretary_people(doc_number)
        elif work_input == 's' or work_input == 'shelf':
            doc_number = input("Введите номер документа:\n")
            secretary_shelf(doc_number)
        elif work_input == 'l' or work_input == 'list':
            secretary_list()
        elif work_input == 'a' or work_input == 'add':
            doc_type = input("Введите тип документа: ")
            doc_number = input("Введите номер документа: ")
            doc_name = input("Введите имя владельца документа: ")
            dic_number = input("Введите номер полки: ")
            print(secretary_add(doc_type,doc_number,doc_name,dic_number))
        elif work_input == 'd' or work_input == 'delete':
            doc_number = input("Введите номер документа:\n")
            secretary_delete(doc_number)
        elif work_input == 'as' or work_input == 'add shelf':
            shelf_number = input("Введите номер полки:\n")
            secretary_add_shelf(shelf_number)
        elif work_input == 'm' or work_input == 'move':
            doc_number = input("Введите номер документа:\n")
            shelf_number = input("Введите номер полки:\n")
            secretary_move(doc_number, shelf_number)
        elif work_input == 'e' or work_input == 'exit':
            break
        else:
            print("Неправильная команда!\n")

