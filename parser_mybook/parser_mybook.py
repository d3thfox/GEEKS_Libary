import requests
from bs4 import BeautifulSoup as BS

URL = 'https://mybook.ru'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS(html, features='html.parser')
    items = bs.find_all('div', class_='e4xwgl-0 iJwsmp')
    mybook_list = []
    for item in items:
        title = item.find('p', class_='lnjchu-1 hhskLb').get_text()
        description = item.find('p', class_='lnjchu-1 dPgoNf').get_text()
        href_tag = item.find('a').get('href')
        href = 'https://mybook.ru' + href_tag
        mybook_list.append({
            'title': title,
            'href': href,
            'description': description
        })
    return loveread_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        mybook_list2 = []
        for page in range(1, 3): 
            response = get_html(f'https://mybook.ru/catalog/books', params={'page': page})
            mybook_list2.extend(get_data(response.text))  
        return mybook_list2  
    else:
        raise Exception('Ошибка парсинга')

