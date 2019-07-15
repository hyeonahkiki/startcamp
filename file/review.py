import csv
import requests
from bs4 import BeautifulSoup
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
res = request.ger(url).text
soup = BeautifulSoup(res, 'html.parser')

tr = soup.selct('tbody > tr')
with open('movierank.csv', 'w', encoding='utf-8', newline = "") as f:
    csv_writer = csv.writer(f)
    for r in tr
        print(r.select _one('.title').text.strip())
        print(r.select_one('.ac').text.)
        row = [r.select _one('.title').text.strip(), r.select_one('.ac').text]
        csv_writer.writerrow(row)