# Функція, яка виводитьусіх в групі через "-"
def print_info(d):
    for i in d:
        print(f"{i} - {d[i]}")

# Відкриваємо  та читаємоо вміст  самого файлу
with open('Txt_for_task_5.txt', "r", encoding="utf-8") as file:
    l = file.read()

# П'ять рядків коду  які видаляєтьт  усе непотрібне
l = l.split('\n')
l = " ".join(l)
l = l.split(" ")
for i in range(1, 21, 2):
    del l[i]

names = []
y_o = []

# 7 рядків коду які переводять числа - в числа, і  додають це все в окремі списки для імен та чисел, окремо.

for i in range(1, 21, 2):#      \
    l[i] = int(l[i])#            \
for i in l:#                      \
    if isinstance(i, int):#        }   ось вони))
        y_o.append(i)#            /
    else:#                       /
        names.append(i)#        /

#  Запис імен та кількість рочків наших учнів до словника де ключем будуть їхні імена, а значеннями кількість рочків
dict_of_all = {}
for i in range(len(names)):
    n = names[i]
    y = y_o[i]
    dict_of_all[n] = int(y)

# Виклик функції :3
print_info(dict_of_all)
print("")
print("")
max_y_o = max(y_o)

# І на останок виведення найстаршого учня та -----------\
for i in dict_of_all:#                                   \
    if dict_of_all[i] == max_y_o:#               ---------\
        print(f"Старший учень:  {i} - {dict_of_all[i]}")#  \
    else:#                                                  |
        continue#                                           /
#Середній вік групи  <----------------------------------___/
o = 0#
for i in y_o:
    o += i
a = o  / len(y_o)
print(f"Середній вік групи {a}")