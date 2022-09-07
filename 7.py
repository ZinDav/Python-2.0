import csv
import json

# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


class PhoneBook:
    def __init__(self):
        self.phone_book = {}
        self.introduction()
    
    def new_contact(self):
        name = input('Input the name of new contact: ')
        num = input('Input the phone of new contact: ')
        if [i for i in self.phone_book.keys() if name == i]:
            shure = input('You already have contact with such name. Are you shure that you want to change\
                 the number? Input Y or N: ')
            if shure == 'Y':
                self.phone_book[name] = num
                print('The contact was changed.')
        elif name in self.phone_book.keys():
            similar_names = [i for i in self.phone_book.keys() if name in i]
            print(f'You already have contacts with similar name: {similar_names}')
            shure = input('Are you shure that you want create new number?\
                 Input Y or N: ')
            if shure == 'Y':
                self.phone_book[name] = num
                print('The new contact was created.')
        else:
            self.phone_book[name] = num
            print('The new contact was created.')
        return self.introduction()

    def delete_contact(self):
        name = input('Input the name of contact that you want to delete: ')
        if [i for i in self.phone_book.keys() if name == i]:
            self.phone_book.pop(name)
            print('The contact was deleted.')
        else:
            print('There is no contact with such name.')
        return self.introduction()

    def change_contact(self):
        name = input('Input the name of contact that you want to change: ')
        if [i for i in self.phone_book.keys() if name == i]:
            dest = int(input('What do you want to chage? 0 - name, 1 - number: '))
            if dest:
                self.phone_book[name] = input('Input new phone of the contact: ')
                print('The contact was changed.')
            elif not dest:
                new_name = input('Input new name of the contact: ')
                self.phone_book[new_name] = self.phone_book.pop(name)
        else:
            print('There is no contact with such name.')
        return self.introduction()

    def import_data(self):
        path = input('Input the path to file: ')
        try:
            with open(path, 'r') as f:
                extens = path.split('.')[-1]
                if extens == 'json':
                    self.phone_book.update(json.load(f))
                elif extens == 'csv':
                    c = csv.reader(f, delimiter=':')
                    self.phone_book.update({i[0]: i[1] for i in c if i})
                elif extens == 'txt':
                    text = json.loads(f.read().replace('\'', '"'))
                    self.phone_book.update(text)
        except:
            print('Input wrong path to file.')
            return self.import_data()
        print(f'Data was imported from {path}.')
        return self.introduction()

    def export_data(self):
        name = input('Input names of contacts that you want to export: ').split(', ')
        if len([i for i in name if i not in self.phone_book.keys()]) > 0:
            print('Input wrong name.')
            return self.export_data()
        try:
            extens = int(input('Input the extension of file. 0 - json, 1 - csv, 2 - txt: '))
        except:
            print('Input not a number.')
            return self.export_data()
        if extens not in [0, 1, 2]:
            print('Input wrong number.')
            return self.export_data()
        path = input('Input the path to file: ')
        dt = {k: self.phone_book[k] for k in name}
        try:
            if not extens:
                with open(f'{path}.json', 'w') as f_json:
                    json.dump(dt, f_json, indent="")
            elif extens == 1:
                with open(f'{path}.csv', 'w') as f_csv:
                    w = csv.writer(f_csv, delimiter=':')
                    w.writerows(dt.items())
            elif extens == 2:
                with open(f'{path}.txt', 'w') as f_txt:
                    f_txt.write(str(dt))
        except:
            print('Input wrong path to file.')
            return self.import_data()
        print(f'Data was exported to {path}.')
        return self.introduction()

    def introduction(self):
        print('\nWhat do you want to do?')
        try:
            but = int(input('0 - show all contacts, \n1 - create new contact, \n2 - delete_contact,\
                \n3 - change contact, \n4 - import data, \n5 - export data, \n6 - exit.\nInput: '))
        except:
            print('Input not a number')
            return self.introduction()
        if but not in (range(0, 7)):
            print('Input number not in 1-6')
            return self.introduction()
        print('')
        if not but:
            for k, v in self.phone_book.items():
                print(f'{k}: {v}')
            return self.introduction()
        elif but == 1:
            self.new_contact()
        elif but == 2:
            self.delete_contact()
        elif but == 3:
            self.change_contact()
        elif but == 4:
            self.import_data()
        elif but == 5:
            self.export_data()
        elif but == 6:
            pass
            

pb = PhoneBook()
