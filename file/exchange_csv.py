import csv
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")

tr = soup.select('tbody > tr')
with open("naver_exchang.csv", 'w', encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    for r in tr :
        print(r.select_one('.tit').text.strip())
        print(r.select_one('.sale').text)
        row = [r.select_one('.tit').text.strip(), r.select_one('.sale').text]
        csv_writer.writerow(row)