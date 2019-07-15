from flask import Flask, request, render_template
from decouple import config
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

api_url = "https://api.telegram.org"
token = config("TELEGRAM_TOKEN")
chat_id = config("CHAT_ID")
naver_id = config("NAVER_ID")
naver_secret = config("NAVER_SECRET")


@app.route('/write')
def write():
    return render_template("write.html")

@app.route("/send")
def send():
    msg = request.args.get("msg")
    url = f"{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    return render_template("send.html")
    res = requests.get(url)

@app.route(f"/{token}", methods=['POST'])
def telegram():
    print(request.get_json())         #json형태로 들어오는 것을 딕셔녀리로 바꿔줌
    data = request.get_json()
    user_id = (data.get("message").get("from").get("id"))
    user_msg = (data.get('message').get('text'))
    
    if data.get('message').get('photo') is None:

        if user_msg == '점심메뉴':
            menu_list = ['삼계탕', '철판낙지볶음밥', '물냉면', '파스타','삼겹살']
            result = random.choice(menu_list)
        elif user_msg =="로또":
            numbers = list(range(1,46))
            result = sorted(random.sample(numbers, 6))
            #result = random.sample(range(1,46),6)
        elif user_msg =="실시간검색어":
            respone = requests.get("https://naver.com").text
            soup = BeautifulSoup(respone,"html.parser")
            naver = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k").text
            result =f"지금 실시간 검색어 1위는 {naver}입니다." 
        elif user_msg =="노래추천":
            music_list = ['백예린_square', 'colde_와르르','prince_ali_willsmith','정승환_눈사람','attention_Charlie Puth']
            music_choice = random.choice(music_list)
            result = f"오늘의 추천 노래는 {music_choice}"
        elif user_msg =='미세먼지':
            respone = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EA%B4%91%EC%A3%BC%20%EB%B6%81%EA%B5%AC%20%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80").text
            soup = BeautifulSoup(respone, 'html.parser')
            dust = int(soup.select_one(".main_figure").text)
            if dust > 150:
                dust_result = "매우나쁨"
            elif dust > 80:
                dust_result = "나쁨"
            elif dust >30:
                dust_result = "보통"    
            else:
                dust_result = "좋음"
            result = f"오늘미세먼지는 {dust}. {dust_result}입니다."
        elif user_msg[0:2]=="번역":
            raw_text = user_msg[3:]
            #번역 안녕하세요 저는 누구입니다.
            #[3:] : 3번부터 끝까지
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            data = {
                "source":"ko",
                "target":"en",
                "text":raw_text
            }
            header = {

                'X-naver-Client-Id':naver_id,
                'X-naver-Client-Secret':naver_secret
            }
            res = requests.post(papago_url, data=data, headers=header)
            translate_res = res.json()
            translate_result = translate_res.get('message').get('result').get('translatedText')
            result = translate_result
        else:
            result = user_msg    
    else:
        #사용자가 보낸 사진을 찾는 과정
        result="okay"
        file_id = data.get('message').get('photo')[-1].get("file_id")
        file_url = (f"{api_url}/bot{token}/getFile?file_id={file_id}")
        file_res = requests.get(file_url)
        file_path = file_res.json().get("result").get('file_path')
        file = f"{api_url}/file/bot{token}/{file_path}"
        print(file)
        #사용자가 보낸 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clova_url = "https://openapi.naver.com/v1/vision/celebrity"
        header = {

                'X-naver-Client-Id':naver_id,
                'X-naver-Client-Secret':naver_secret
            }

        clova_res = requests.post(clova_url, headers=header, files={'image':res.raw.read()})

        if clova_res.json().get('info').get('faceCount'):
            #누구랑 닮았는지 출력
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            name = celebrity.get('value')
            confidence = celebrity.get('confidence')
            result = f"{name}일 확률이 {confidence*100}%입니다."
        else:
            #사람이 없음
            result = "사람이 없습니다."            

     

    res_url = f"{api_url}/bot{token}/sendMessage?chat_id={user_id}&text={result}"
    requests.get(res_url)
    
    return "", 200



if __name__=="__main__":
    app.run(debug=True)