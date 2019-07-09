import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select('#KOSPI_now')
print(kospi.text)