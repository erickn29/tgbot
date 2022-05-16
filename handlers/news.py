import datetime
import requests
from bs4 import BeautifulSoup as bs


def get_football_news():
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://www.sports.ru/football/topnews/'
    no_parse_titles = [
        'Чемпионат Италии',
        'Чемпионат Испании',
        'Чемпионат Англии',
        'Чемпионат Германии',
        'Чемпионат Франции',
        'Чемпионат России',
        'новости утра',
        'другие новости'
    ]
    print('Начинаю парсинг')
    news_list = ''
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser")
        for link in soup.findAll('a', class_='short-text')[0:30]:
            if 'http' in link.get('href'):
                continue
            if link.text.split('.')[0] in no_parse_titles:
                continue
            news_title = link.text.split('.')[0]
            news_donor = f"https://www.sports.ru{link.get('href')}"
            news_list += f'[{news_title}]({news_donor})\n\n'
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)
        return None


def get_soc_news():
    news_list = ''
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://www.rbc.ru/society/?utm_source=topline'
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser")
        for link in soup.findAll('a', class_='item__link'):
            news_title = link.text.strip()
            news_donor = link.get('href')
            news_list += f'[{news_title}]({news_donor})\n\n'
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)
        return None


def get_politics_news():
    news_list = ''
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://www.rbc.ru/politics/?utm_source=topline'
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser")
        for link in soup.findAll('a', class_='item__link'):
            news_title = link.text.strip()
            news_donor = link.get('href')
            news_list += f'[{news_title}]({news_donor})\n\n'
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)
        return None


def get_econamics_news():
    news_list = ''
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://www.rbc.ru/economics/?utm_source=topline'
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser")
        for link in soup.findAll('a', class_='item__link'):
            news_title = link.text.strip()
            news_donor = link.get('href')
            news_list += f'[{news_title}]({news_donor})\n\n'
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)
        return None


def get_tech_news():
    news_list = ''
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://www.ixbt.com/news/'
    news_list = ''
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser")
        for li in soup.findAll('li', class_='item')[0:20]:
            for link in li.find_all('a'):
                if 'comments' in link.get('href'):
                    continue
                url = link.get("href")
                txt = link.text.strip()
                news_list += f'[{txt}](https://www.ixbt.com{url})\n\n'
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)


def get_games_news():
    news_list = ''
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://ixbt.games/news/'
    news_list = ''
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser")
        for link in soup.findAll('a', class_='card-link')[0:20]:
            # print(link.get('href'))
            # print(link.text.strip())
            news_list += f"[{link.text.replace('[Видео] ', '').strip()}](https://ixbt.games{link.get('href')})\n\n"
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)


def get_arh_afisha():
    news_list = ''
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://arh.kassir.ru/'
    news_list = ''
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser").find_all('div', class_='new--w-12')
        for link in soup[0:20]:
            title = link.find('div', class_='title').find('a').text.strip()
            url = link.find('div', class_='title').find('a').get('href')
            date = link.find('nobr').text.replace('  ', '').strip()
            place = link.find('div', class_='venue').find('a').text.strip()
            price = f"₽ {link.find('div', class_='cost').text.strip()}"
            news_list += f'[{title}]({url})\n{date}\n{place}\n{price}\n\n'
            # news_list += f"[{link.text.replace('[Видео] ', '').strip()}](https://ixbt.games{link.get('href')})\n\n"
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)


def get_arh_news():
    news_list = ''
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br'
    }
    URL = 'https://www.news29.ru/#newsLine'
    news_list = ''
    try:
        response = requests.request('GET', URL, headers=HEADERS).text
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Получил ответ от {URL}')
        soup = bs(response, "html.parser").find_all('div', class_='title')
        for div in soup[0:20]:
            news_list += f'[{div.find("a").text.strip()}](https://www.news29.ru{div.find("a").get("href")})\n\n'
            # news_list += f"[{link.text.replace('[Видео] ', '').strip()}](https://ixbt.games{link.get('href')})\n\n"
        print(f'[{datetime.datetime.now().time().strftime("%H:%M:%S")}]Отдаю результат')
        return news_list
    except Exception as e:
        print(e)
