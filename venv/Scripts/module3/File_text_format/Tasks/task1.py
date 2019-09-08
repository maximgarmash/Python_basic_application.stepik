import csv
Primary_Type = []
Primary_Type_number = set()

with open("Crimes.csv", "r") as f:
    crimes = csv.reader(f)
    for row in crimes:
        if "2015" in row[2]:
            Primary_Type.append(row[5])
            Primary_Type_number.add(row[5])

number_dict = {Primary_Type.count(type_crime): type_crime for type_crime in Primary_Type_number}
print(number_dict[max(number_dict.keys())])

#               Пример изящного решения
#
# from collections import Counter as c
#
# with open('Crimes.csv') as f
#     data = csv.reader(f)
#     print(c( row[5] for row in data if '2015' in row[2] ))