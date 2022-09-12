import csv
import json

# Создать информационную систему позволяющую работать с сотрудниками некой компании

class Base():
    def __init__(self):
        self.employer_base = {}
        
    def determine_eid(self):
        if self.employer_base:
            return max(self.employer_base.keys()) + 1
        else:
            return 1

    def recognize_eid(self):
        check = input('Do you know eid of the employer? (Y/N): ')
        if check == 'Y':
            try:
                eid = int(input('Input eid of the employer: '))
            except:
                print('Input non number.')
                return self.recognize_eid()
            if eid not in self.employer_base.keys():
                print('Input eid is not exists.')
                return self.recognize_eid()
        elif check == 'N':
            name = ''
            surname = ''
            department = ''
            ch_eid = 0
            while not ch_eid:
                if type(ch_eid) is list:
                    print('Employer with input name, surname and department is not exists.')
                name = input('Input name of the employer: ')
                surname = input('Input surname of the employer: ')
                department = input('Input department for the employer: ')
                ch_eid = [k for k, v in self.employer_base.items() if v[0] == name and v[1] == surname \
                    and v[4] == department]
            eid = ch_eid[0]
        else:
            return self.recognize_eid()
        return eid
    
    def hire_employer(self):
        name = input('Input name of the new employer: ')
        surname = input('Input surname of the new employer: ')
        birthday = input('Input birthday of the new employer in format dd.mm.yyyy: ')
        position = input('Input position of the new employer: ')
        department = input('Input department for the new employer: ')
        try:
            salary = float(input('Input salary size for the new employer: '))
            premium = float(input('Input premium for the new employer: '))
        except:
            print('Input non number.')
            return self.hire_employer()
        self.employer_base[self.determine_eid()] = \
            [name, surname, birthday, position, department, salary, premium]
        return [name, surname, birthday, position, department, salary, premium]

    def change_employer(self):
        eid = self.recognize_eid()
        p = ''
        titles = ['name', 'surname', 'birthday', 'position', 'department', 'salary', 'premium']
        while p not in titles:
            p = input('Input part name what you want to change. \
                \nSelect one of the (name, surname, birthday, position, department, salary, premium): ')
        ind = [n for n, i in enumerate(titles) if p == i]
        self.employer_base[eid][ind[0]] = input('Input changing in selected part: ')
        return titles[ind[0]]

    def dismiss_employer(self):
        eid = self.recognize_eid()
        return self.employer_base.pop(eid)
    
    def raise_salary(self):
        emps = input('Who do you want to raise a salary for? (1 - for the employer, 2 - for the department): ')
        if emps not in ['1', '2']:
            return self.raise_salary()
        elif emps == '1':
            eid = [self.recognize_eid()]
        elif emps == '2':
            depart = input('Input the department: ')
            eid = [k for k, v in self.employer_base.items() if v[4] == depart]
        raised = float(input('Input the percent on which you want to raise a salary: '))/100 + 1
        for i in eid:
            self.employer_base[i][5] = round(raised * self.employer_base[i][5], 2)
    
    def put_premium(self):
        emps = input('Who do you want to put a premium for? (1 - for the employer, 2 - for the position): ')
        if emps not in ['1', '2']:
            return self.put_premium()
        elif emps == '1':
            eid = [self.recognize_eid()]
        elif emps == '2':
            posit = input('Input the position: ')
            eid = [k for k, v in self.employer_base.items() if v[4] == posit]
        prem = float(input('Input the premium: '))
        for i in eid:
            self.employer_base[i][6] = prem
    
    def count_monthly_salary(self):
        return sum([i[5] for i in self.employer_base.values()])
    
    def import_data(self):
        path = input('Input the path to file: ')
        try:
            with open(path, 'r') as f:
                extens = path.split('.')[-1]
                if extens == 'json':
                    self.employer_base.update(json.load(f))
                elif extens == 'csv':
                    c = csv.reader(f, delimiter=':')
                    self.employer_base.update({i[0]: i[1] for i in c if i})
                elif extens == 'txt':
                    text = json.loads(f.read().replace('\'', '"'))
                    self.employer_base.update(text)
        except:
            print('Input wrong path to file.')
            return self.import_data()
        return path

    def export_data(self):
        check = 0
        eid = []
        while check != 'N':
            eid.append(self.recognize_eid())
            check = input('Do you want to continue input data of the employer? Input N to stop typing: ')
        extens = input('Input the extension of file. 0 - json, 1 - csv, 2 - txt: ')
        if extens not in ['0', '1', '2']:
            print('Input wrong number.')
            return self.export_data()
        path = input('Input the path to file: ')
        dt = {k: self.employer_base[k] for k in eid}
        try:
            if extens == '0':
                with open(f'{path}.json', 'w') as f_json:
                    json.dump(dt, f_json, indent="")
            elif extens == '1':
                with open(f'{path}.csv', 'w') as f_csv:
                    w = csv.writer(f_csv, delimiter=':')
                    w.writerows(dt.items())
            elif extens == '2':
                with open(f'{path}.txt', 'w') as f_txt:
                    f_txt.write(str(dt))
        except:
            print('Input wrong path to file.')
            return self.import_data()
        return path