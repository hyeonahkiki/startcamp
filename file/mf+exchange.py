import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_EURKRW"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
exchange = soup.select_one("#content > div.spot > div.today > p.no_today").text

with open("exchange.txt", 'w') as f:
    f.write(exchange.strip())
