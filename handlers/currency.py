import datetime
import requests
from bs4 import BeautifulSoup as bs


def get_currency():
    cur_list = 'Курсы валют на данную минуту:\n\n'
    HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'accept-encoding': 'gzip, deflate, br'
            }
    URL1 = 'https://www.cbr.ru/currency_base/daily/'
    URL2 = 'https://coinmarketcap.com/'

    CUR = ['USD', 'EUR', 'CNY', 'GBP',]
    CRY = ['BTC', 'ETH',]

    response = requests.request('GET', URL1, headers=HEADERS).text
    soup = bs(response, "html.parser").find_all('tr')
    for tr in soup:
        for data in tr.find_all('td'):
            for val in CUR:
                if val in data:
                    # print(f'1 {tr.contents[3].text.strip()} = {tr.contents[9].text.strip()} RUB')
                    cur_list += f'1 {tr.contents[3].text.strip()} = {tr.contents[9].text.strip()} RUB\n'
    cur_list += '\n'
    response = requests.request('GET', URL2, headers=HEADERS).text
    soup = bs(response, "html.parser").find_all('tr')
    cycles = 0
    cry_num = 0
    for tr in soup:
        if cycles > 1:
            break
        for val in CRY:
            if val in tr.contents[2].text:
                cycles += 1
                # print(f'1 {CRY[cry_num]} = {tr.contents[3].text.replace("$", "")} {CUR[0]}')
                cur_list += f'1 {CRY[cry_num]} = {tr.contents[3].text.replace("$", "")} {CUR[0]}\n'
                cry_num += 1
    return cur_list

