import re
from bs4 import BeautifulSoup
pattern  = r"[A-Za-z0-9]+(?:\.[a-zA-Z0-9]+)*@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+"

def isValid(email):
    if re.fullmatch(pattern, email):
      print(f"Valid email : {email}")
    else:
      print(f"Invalid email : {email}")

soup = BeautifulSoup(open("storage.html"), 'html.parser')
for link in soup.find_all('a'):
    link = link.get('href')[7:] #link.get('href') выводит mailto:test@test.ru и чтобы убрать mailto: срезаем 7 символов
    isValid(link)

