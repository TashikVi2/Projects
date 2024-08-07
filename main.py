# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
from csv import DictWriter, DictReader
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

# ф-ция для получения списка 
def get_data():
    flag = False
    while not flag:
        try:
            first_name =input("введите имя:   ")
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            last_name =input("введите Фамилию:   ")
            if len(last_name) < 2:
                raise NameError('Слишком короткая фамилия')
            phone=input("введите телефон:   ")
            if len(phone) < 8:
                raise NameError('Слишком короткий номер')
        except NameError as err:
            print(err)
        else:
            flag= True
        
    # first_name ="ivan J"
    # last_name ="boss"
    # phone="+74444444"
    return [first_name, last_name,  phone]

#ф-ция для создания файла
def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

# ф-ция для чтения файла
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)
    
# ф-ция для записи файла
def write_file(filename, lst):
    res =  read_file(filename)
    obj = {'Имя':lst[0], 'Фамилия':lst[1],'Телефон':lst[2] }
    res.append(obj)
    standard_write(filename,res)


#реализуем поиск по фамилии       
def row_search(filename):
    last_name = input("введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            return row      
    return "Запись не найдена"  

def delete_row(filename):
    row_number = int(input("введите номер строки для удаления:   "))
    res = read_file(filename)
    res.pop(row_number-1)
    standard_write(filename, res)
#выносим стандартные части функций в отдльную функцию        
def standard_write(filename, res):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)
#изменяем строку по команде
def change_row(filename):
    row_number = int(input("введите номер строки для изменения:   "))
    res = read_file(filename)
    res[row_number-1]["Имя"] = data[0]
    res[row_number-1]["Фамилия"] = data[1]
    res[row_number-1]["Телефон"] = data[2]
    standard_write(filename, res)
    

# копируем строку по команде(д/з)

def copy_row_to_file(filename, target_file):
    res = read_file(filename)
    line_number = int(input("введите номер строки для копирования:   "))
   
    try:
        line_to_copy = res[line_number - 1]  # Нумерация строк начинается с 0
    except IndexError:
        print("Ошибка: указанной строки не существует в исходном файле.")
        return

    with open(target_file, 'a') as f_target:  # Открываем файл для добавления (append)
        f_target.write(str(line_to_copy))
        # print(line_to_copy)

    print(f"Строка {line_number} успешно скопирована из {filename} в {target_file}.")

# Пример использования функции
# source_file = "source.txt"
# target_file = "target.txt"
# line_number = int(input("Введите номер строки для копирования: "))

# copy_line(source_file, target_file, line_number)

filename = 'phone.csv'
target_file = 'new_phone.csv'

def main():
    while True:
        command = input("введите команду f- поиск, с - изменить строку, r- прочитать, w-записать, copy - скопировать строку: ")
        # command="r"
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":
            if not exists(filename):
                print("файла нет. Создайте его")
                continue
            print(read_file(filename))
 #код для поиска файла             
        elif command == "f":
            if not exists(filename):
                print("файла нет. Сздайте его")
                continue
            print(row_search(filename))
 #код для удаления файла       
        elif command == "d":
            if not exists(filename):
                print("файла нет. Сздайте его")
                continue
            delete_row(filename)

#код для внесения изменений 
        elif command == "c":
            if not exists(filename):
                print("файла нет. Сздайте его")
                continue
            change_row(filename)
#код для запуска копирования:
        elif command == "copy":
                    if not exists(filename):
                        print("файла нет. Сздайте его")
                        continue
                    copy_row_to_file(filename, target_file )
main()



