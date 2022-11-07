# 11. Из документа HTML вывести все e-mail.
import re
from bs4 import BeautifulSoup
pattern  = r"[A-Za-z0-9-_+]+(?:\.[a-zA-Z0-9_+-]+)*@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+"
HTMLFile = open("storage.html", "r")

soup = BeautifulSoup(HTMLFile, 'lxml')
match = re.findall(pattern, soup.get_text())
for link in soup.find_all('a'):
    href = link.get('href')[7:]
                                #link.get('href') выводит mailto:test@test.ru
                                #и  чтобы убрать mailto: срезаем 7 символов
    if href in match:
        print(href)
