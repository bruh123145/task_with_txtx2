list_au = []
with open("quotes_2.txt", "w", encoding="utf-8") as file:
    file.write("""
Садок вишневий коло хати,
Хрущі над вишнями гудуть,
Плугатарі з плугами йдуть,
Співають ідучи дівчата,
А матері вечерять ждуть.
    """)
with open('quotes_2.txt', "r", encoding="utf-8") as file:
    s = file.read()
print(s)
au = input('Хто написав ці рядки?')
list_au.append(au)
que = input('Хочете додати цитату? (так/ні) ')
while que != "ні":
    quote = input('Введіть цитату: ')
    au_2 = input('Введіть автора: ')
    list_au.append(au_2)
    que = input('Хочете додати цитату? (так/ні) ')
with open('quotes_2.txt', 'w', encoding="utf-8") as file:
    for i in list_au:
        file.write(f"({i})\n")
with open('quotes_2.txt', "r", encoding='utf-8') as file:
    f = file.read()
print(f)