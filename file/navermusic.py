import csv
import requests
from bs4 import BeautifulSoup
url = "https://music.naver.com/"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')

tr = soup.select('tbody > tr')
with open("naver_music.csv", 'w', encoding='utf-8', newline = "") as f:
    csv_writer = csv.writer(f)
    for r in tr :
        print(r.select_one('.m_ell').text.strip())
        print(r.select_one('._artist').text)
        row = [r.select_one('.m_ell').text.strip(), r.select_one('._artist').text]
        csv_writer.writerow(row)