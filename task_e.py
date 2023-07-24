#------------------------------------------------------------------------------------
import csv
#------------------------------------------------------------------------------------
def read_csv_and_create_dict(csv_file):
    data_dict = {}

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            gender = row['Gender']
            age = int(row['Age'])
            salary = float(row['Salary'])

            # Создание вложенного словаря для каждого имени
            info_dict = {
                'Gender': gender,
                'Age': age,
                'Salary': salary
            }

            # Добавляем словарь в итоговый словарь с именем в качестве ключа
            data_dict[name] = info_dict

    return data_dict
#------------------------------------------------------------------------------------
# Входные данные
csv_file = 'data_e.csv'
result_dict = read_csv_and_create_dict(csv_file)
#------------------------------------------------------------------------------------
# Выводим полученный словарь
print(result_dict,'\n')
#------------------------------------------------------------------------------------