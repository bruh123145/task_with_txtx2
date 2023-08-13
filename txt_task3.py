with open("quotes3.txt", "w", encoding="utf-8") as file:
    file.write("""Садок вишневий коло хати,
Хрущі над вишнями гудуть,
Плугатарі з плугами йдуть,
Співають ідучи дівчата,
А матері вечерять ждуть.
""")
while True:
    name_file = input("Введіть ім'я файла: ")
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            filee = file.read()
        break
    except IOError:
        print('Такого файлу не існу! Повторіть введення.')
        name_file = input("Введіть ім'я файла: ")
print(filee)
au_qu = input('Хто написав ці рядки? ')
with open("quotes3.txt", "a", encoding="utf-8") as file:
    file.write(f"({au_qu}) \n")
que = input('Хочете додати цитату? (так/ні) ')
while que != "ні":
    quote = input('Введіть цитату: ')
    au_2 = input('Введіть автора: ')
    with open("quotes3.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{quote}")
        file.write(f"\n({au_2})")
    que = input('Хочете додати цитату? (так/ні) ')
with open('quotes3.txt', "r", encoding="utf-8") as file:
    for i in file:
        print(i)
a = input('')