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
        f_w = DictWriter(data, filenames = ['Имя', 'Фамилия', 'Телефон'])
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
    standard_write(filename)


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
    data = get_data()
    res[row_number-1]["Имя"] = data[0]
    res[row_number-1]["Фамилия"] = data[1]
    res[row_number-1]["Телефон"] = data[2]
    standard_write(filename, res)
    

#копируем строку по команде(д/з)
# def copy_row_to_file(filename, res, new_file):
#     row_number = int(input("введите номер строки для копирования:   "))
#     res = read_file(filename)
#     res[row_number-1]["Имя"] = new_file[0]
#     res[row_number-1]["Фамилия"] = new_file[1]
#     res[row_number-1]["Телефон"] = new_file[2]
#     obj = {'Имя':new_file[0], 'Фамилия':new_file[1],'Телефон':new_file[2] }
    
#     standard_write(new_file, res)
#     res2 =  read_file(new_file)
#     obj = {'Имя':row[0], 'Фамилия':row[1],'Телефон':row[2] }
#     res2.append(obj)

filename = 'phone.csv'

def main():
    while True:
        command = input("введите команду:")
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
                    copy_row_to_file(filename, res, new_file)
main()




