import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

correct_list = []
for contact in contacts_list:
    fio = ' '.join(contact[:3]).split(' ')
    contact[0:3] = fio[0:3]
    pattern   = r"(\+7|8)?(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\-*)(\d{2})(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)"
    substitution = r"+7(\4)\8-\10-\12\13\15\16\18"
    rez = re.sub(pattern, substitution, contact[5])
    contact[5] = rez
    correct_list.append(contact)
#print(correct_list)


final_list = []
group_list = []
for key in correct_list:
    if key[0:2] not in final_list:
        final_list.append(key[0:2])
        group_list.append([key[2:]])
    else:
        count = final_list.index(key[0:2])
        group_list[count].append(key[2:])

for i, element in enumerate(group_list):
    if len(element) > 1:
        concat = list(zip(element[0], element[1]))
        for j, elem in enumerate(concat):
            if elem[0] == elem[1]:
                concat[j] = elem[0]
            elif elem[0] == "":
                concat[j] = elem[1]
            elif elem[1] == "":
                concat[j] = elem[0]
        group_list[i] = concat
    else:
        group_list[i] = [item for i in element for item in i]

for i, name in enumerate(final_list):
    final_list[i] = name + group_list[i]



pprint(final_list)





with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(final_list)