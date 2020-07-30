from pprint import pprint
from lxml import html
import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
main_link = 'https://lenta.ru/'

response = requests.get(main_link,headers=header)
dom = html.fromstring(response.text)

lentanews = dom.xpath("//div[@class='span4']/div[@class='item'] | //div[@class='span4']/div[@class='first-item']")

news = []
for lenta in lentanews:
    new = {}
    source = 'lenta.ru'
    name = lenta.xpath(".//div[@class='item']/a/text()")
    link = lenta.xpath(".//div[@class='span4']/div[@class='item']/a[@href]")
    date = lenta.xpath(".//time[@title]/text()")[0]

    new['source'] = source
    new['name'] = name
    new['link'] = link
    new['date'] = date

    news.append(new)

main_link = 'https://yandex.ru/'

response = requests.get(main_link,headers=header)
dom = html.fromstring(response.text)

yandexnews = dom.xpath("//ol/li")

yanews = []
for yandex in yandexnews:
    newsyandex = {}
    source = 'yandex.ru'
    name = yandex.xpath(".//ol//a/text()")
    link = yandex.xpath(".//ol/li/a[@href]")
    date = yandex.xpath("//span[contains(@class,'datetime__date')]")

    newsyandex['source'] = source
    newsyandex['name'] = name
    newsyandex['link'] = link
    newsyandex['date'] = date

    news.append(newsyandex)

pprint(news)