import requests
from bs4 import BeautifulSoup as BS
import json

URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=1"


r = requests.get(URL_TEMPLATE)

soup = BS(r.text, "html.parser")
vacancies_names = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link js-hot-block')
vacancies_info = soup.find_all('p', class_='overflow text-muted add-top-sm add-bottom')
_vacancies = zip(vacancies_names, vacancies_info)
vacancies = {vacancies_[0]: vacancies_[1] for vacancies_ in _vacancies}
for info in vacancies.items():
    print('---'*5)
    print(info[0].h2.a['title'])
    print('https://www.work.ua'+info[0].a['href'])
    print(info[1].text)
    print('---'*5)
_vacancies = zip(vacancies_names, vacancies_info)
vacancies = {str(vacancies_[0].h2.a['title']): vacancies_[1].text for vacancies_ in _vacancies}
print(vacancies)
