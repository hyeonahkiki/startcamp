import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")

tr = soup.select('tbody > tr')
for r in tr :
    print(r.select_one('.tit').text.strip())
    print(r.select_one('.sale').text)