import csv
import requests
from bs4 import BeautifulSoup
url = "https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')

tr = soup.select('tbody > tr')
with open("bithumb.csv", 'w', encoding='utf-8', newline = "") as f:
    csv_writer = csv.writer(f)
    for r in tr
        print(r.select_one('a').text.strip())
        print(r.select_one('.sort_real').text)
        row = [r.select_one('a').text.strip(), r.select_one('.sort_real').text]
        csv_writer.writerow(row)