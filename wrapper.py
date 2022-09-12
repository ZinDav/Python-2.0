from base import Base

def wrapper():
    base = Base()
    k = ''
    while k != '12':
        k = input('\nWhat do you want to do?\n1 - show all employers,\n2 - show all departments, \
            \n3 - hire new employer,\n4 - find eid of the employer,\n5 - change the employer,\
            \n6 - dismiss the employer,\n7 - raise a salary,\n8 - put a premium,\
            \n9 - count monthly salary,\n10 - import data,\n11 - export data,\n12 - exit. \nInput: ')
        if k == '1':
            print('All employers:\n',*[i for i in base.employer_base.values()], sep='\n')
        elif k == '2':
            print(f'All departments:\n{[i[4] for i in base.employer_base.values()]}', sep='\n')
        elif k == '3':
            e = base.hire_employer()
            print(f'Employer {e[0]} {e[1]} was added in base.')
        elif k == '4':
            print(f'{base.recognize_eid()} is eid of the employer.')
        elif k == '5':
            print(f'{base.change_employer()} was changed.')
        elif k == '6':
            de = base.dismiss_employer()
            print(f'{de[0]} {de[1]} was dismissed.')
        elif k == '7':
            base.raise_salary()
            print('The salary was raised.')
        elif k == '8':
            base.put_premium()
            print('The premium was putting.')
        elif k == '9':
            print(f'The sum of monthly salaries is {base.count_monthly_salary()}.')
        elif k == '10':
            print(f'Data was imported from {base.import_data()}.')
        elif k == '11':
            print(f'Data was exported to {base.export_data()}.')
