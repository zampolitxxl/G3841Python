def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')
    if choice == 7: #works
            print_result((f'Работа закончена'))
    while (choice != 7):
        if choice == 1: #works
            print_result(phone_book)
        elif choice == 2: #works
            surname = get_search_surname()
            print(find_by_surname(phone_book, surname))
        elif choice == 3: #works
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4: #works
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)  
        elif choice == 6:
            surname = get_search_surname()
            newres = del_by_surname(phone_book, surname)
            write_csv('phonebook.csv', newres)
            phone_book = newres
            print("Абонент удален ")
                 
        choice = show_menu()  
        
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента по фамилии\n"
          "7. Закончить работу")
    return int(input())

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Комментарий"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, pb: list):
    with open(filename, 'w', encoding= 'utf-8') as fout:
        for i in range(len(pb)):
            s=' '
            for v in pb[i].values():
                s+=v+','
            fout.write(f'{s[:-1]}\n') #удаляем последний элемент 

#Функция принт резалт
def print_result(phone_book: list):
    print(phone_book)
    print(*phone_book[0].keys())
    for i in range(len(phone_book)):
        s=' '
        for v in phone_book[i].values():
            s+='%-15s' %v
        print(f'{s[:-1]}\n')




#Функция get_search_surname функция введения фамилии для поиска

def get_search_surname():
    return input("Введите, фамилию для поиска")

def find_by_surname(pb, familia):
    print(next(x for x in pb if x["Фамилия"] == familia))

def get_search_number():
    return input("Введите, номер для поиска")

def find_by_number(pb, number):
    print(next(x for x in pb if x["Телефон"] == number))

#Choice 4

def get_new_user():
    newuser = []
    newuser.append(input("\nВведите, фамилию нового пользователя"))
    newuser.append(input("\nВведите, имя нового пользователя"))
    newuser.append(input("\nВведите, номер нового пользователя"))
    newuser.append(input("\nВведите, описание нового пользователя"))
    return (newuser)

def add_user(pb, user_data):
    fields = ["Фамилия", "Имя", "Телефон", "Комментарий"]
    zap = dict(zip(fields, user_data))
    pb.append(zap)


#Choice 5
def get_file_name():
    return input("Введите, название файла")

def write_txt(file_name, phone_book):
    with open(file_name, "w") as my_output_file:
        for i in range(len(phone_book)):
            s=' '
            for v in phone_book[i].values():
                s+=v+','
            my_output_file.write(f'{s[:-1]}\n') #удаляем последний элемент

#Choice 6

#def del_by_surname(phone_book, surname):
 #   print(phone_book)
  #  for i in range(len(phone_book)):
   #     print(i)
    #    for v in phone_book[i].values():
     #       print(v)
      #      if v == surname:
       #         delit= i
    #phone_book.pop(delit)

def del_by_surname(phone_book, surname):
    res = []
    for line in phone_book:
        if surname !=line['Фамилия']:
            res.append(line)
    return res


work_with_phonebook()















