import webbrowser

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
my_keywords = ["blockb", "bts", "winner", "shinee"]
for i in my_keywords:
    print(i)
    webbrowser.open_new_tab(url + i)