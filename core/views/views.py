from django.shortcuts import render
from core.models import Car
from core.models import Profession
from core.models import Image
import requests
import json
import re

def index(request):
    context = {
        'cars': Car.objects.all(),
        'professions': Profession.objects.all(),
    }
    return render(request, 'core/index.html', context)

def test(request):
    context = {}
    return render(request, 'core/test.html', context)

def statistic(request):
    context = {'images':Image.objects.all()}
    return render(request, 'core/statistic.html', context)



def api(request):
    jsons = json.loads(getPage())['items']
    class Vacancy:
        def __init__(self, url, published_at, name, description):
            self.url = url
            self.published_at = published_at
            self.name = name
            self.description = description
    def clear(x):
        lst = re.sub(r"<[^>]+>", '', x).split()
        return ' '.join(lst)
    vacancies = []
    for item in jsons:
        value = json.loads(getDescription(item['url']))
        desc = clear(value['description'])
        vacancies.append(Vacancy(item['alternate_url'],item['published_at'], item['name'], desc[:150]+'...'))
    vacancies = vacancies[:10]
    vacancies.reverse()
    context = { 'vacancies':vacancies}
    return render(request, 'core/api.html', context)

def getPage():
    params = {
        'text': 'NAME:Аналитик', # Текст фильтра. В имени должно быть слово "Аналитик"
        'page': 0, # Индекс страницы поиска на HH
        'per_page': 100 # Кол-во вакансий на 1 странице
    }
    req = requests.get('https://api.hh.ru/vacancies', params) # Посылаем запрос к API
    data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data

def getDescription(link):
    req = requests.get(link)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data