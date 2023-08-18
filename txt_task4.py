import time
start_time = time.time()
with open("list_of_students", 'r', encoding="utf-8") as file:
    marks = file.read()
marks = marks.split(' ')
surenames = ["Іванов О.", "Сидорчук И.", "Ковганич Н.", "Коцюба О.", "Українець В.", "Ревера Д.", "Гриць Н.", "Данилів П.", "Оранський В.", "Левчук Ю.", "Олегів К"]
def print_txt(d):
    for i in d:
        print(f"{i} - {d[i]}")
def print_marks_students(d):
    for i in d:
        if d[i] == 5:
            print(i)
        else:
            continue
def average_mark():
    o = 0
    for i in marks:
         o = o + int(i)
    a = o / len(marks)
    return str(a)
dict_s_m = {}
for i in range(len(surenames)):
    s = surenames[i]
    m = marks[i]
    dict_s_m[s] = int(m)
print_txt(dict_s_m)
for i in range(3):
    print("")
print("Відмінники")
print_marks_students(dict_s_m)
print("")
print("")
print("Середня оцінка класу: ", average_mark())
end_time = time.time()
t = end_time - start_time
print(f"Час виконання: {t}")