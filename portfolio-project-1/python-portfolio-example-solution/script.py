import csv
from matplotlib import pyplot as plt

ages = []
sex = []
bmis = []
children_amt = []
smoker = []
region = []
charges = []
csv_data = 'portfolio-project-1/python-portfolio-example-solution/insurance.csv'

def load_lists(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

load_lists(ages, csv_data, 'age')
load_lists(sex, csv_data, 'sex')
load_lists(bmis, csv_data, 'bmi')
load_lists(children_amt, csv_data, 'children')
load_lists(smoker, csv_data, 'smoker')
load_lists(region, csv_data, 'region')
load_lists(charges, csv_data, 'charges')

male_smokers_list = []
female_smokers_list = []
non_smokers_list = []
def load_smokers_list(lst1, lst2, lst3, csv_file):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            if row['smoker'] == 'yes' and row['sex'] == 'female':
                lst1.append({'age': row['age'],
                            'sex': row['sex'],
                            'smoker': row['smoker'],
                            'bmi': row['bmi'],
                            'region': row['region']})
            elif row['smoker'] == 'yes' and row['sex'] == 'male':
                lst2.append({'age': row['age'],
                            'sex': row['sex'],
                            'smoker': row['smoker'],
                            'bmi': row['bmi'],
                            'region': row['region']})
            else:
                lst3.append({'age': row['age'],
                            'sex': row['sex'],
                            'smoker': row['smoker'],
                            'bmi': row['bmi'],
                            'region': row['region']})
        return lst1, lst2

age_child_list = []
def load_age_child_list(lst, csv_file):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            if int(row['children']) > 0:
                lst.append({'age': row['age'],
                            'sex': row['sex'],
                            'children_amt': row['children']})
        return lst

load_smokers_list(female_smokers_list, male_smokers_list, non_smokers_list, csv_data)
load_age_child_list(age_child_list, csv_data)

print(female_smokers_list)


# print(age_child_list)
