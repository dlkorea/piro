import requests
from bs4 import BeautifulSoup as Soup

base_url = 'http://comic.naver.com'
url_path = '/webtoon/list.nhn?titleId=20853&weekday=tue&page='
page = 1

url = base_url + url_path + str(page)

r = requests.get(url)
if r.status_code == 200:
    soup = Soup(r.text)
    title_td_list = soup.find_all(class_='title')
    title = title_td_list[0].a.get_text()
    href = base_url + title_td_list[0].a.attrs['href']
