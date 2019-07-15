from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/") #route 경로를 받아주는것. /: 하나만 있다는 거는 최상단의 의미. 서버 주소 그 자체. ctrl +c 서버 꺼지는키
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "안녕하세요!!!"

@app.route("/html_tag")
def html_tag():
        return "<h1>안녕하세요</h1>"

@app.route("/html_tags")
def html_tags():
    return """
    <h1>안녕하세요</h1>
    <h2>반갑습니다</h2>
    """
import datetime
@app.route("/dday")
def dday():
    today = datetime. datetime.now()
    endday = datetime.datetime(2019,11,29)
    d = endday-today
    return f"1학기 종료까지 {d.days}일 남음!!"

@app.route("/html_file")
def html_file():
    return render_template('index.html')

@app.route("/greeting/<string:name>")#string 문자 / 변수 name
def greeting(name):
    return f"안녕하세요 {name}님!!"

@app.route("/cube/<int:num>")
def cube(num):
    cube_num = num**3 #세제곱표현
    return f"{num}의 세제곱은 {cube_num}입니다."

@app.route("/cube_html/<int:num>")
def cube_html(num):
    cube_num = num**3
    return render_template("cube.html", num_html=num, cube_num_html=cube_num)


@app.route("/greeting_html/<string:name>")
def greeting_html(name):
    return render_template("greeting.html", name=name)


@app.route("/lunch")
def lunch():
    menu = {
        "짜장면":"http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg",
        "짬뽕":"https://upload.wikimedia.org/wikipedia/commons/b/bb/Jjamppong.jpg",
        "스파게티":"http://ko.sukpasta.wikidok.net/api/File/Real/578c682d5e1a20ee46f0264e",
    }

    menu_list= list(menu.keys()) #["짜장면", "짬뽕", "스파게티"]    
    pick = random.choice(menu_list)
    img = menu[pick]

    return render_template("lunch.html", pick=pick, img=img)

@app.route('/movies')
def movies():
    movie_list = ['알라딘', '존윅', '스파이더맨','토이스토리4']
    return render_template("movies.html", movie_list=movie_list)


@app.route('/ping')
def ping():
        return render_template("ping.html")

@app.route('/pong')
def pong():
        user_input = request.args.get("test")      
        return render_template("pong.html", user_input=user_input)

@app.route("/naver")
def naver():
        return render_template("naver.html")

@app.route("/google")
def google():
        return render_template("google.html")

@app.route("/text")
def text():
        return render_template("text.html")

import requests
@app.route("/result")
def result():
        raw_text = request.args.get("raw")
        url = "http://artii.herokuapp.com/make?text="
        res = requests.get(url+raw_text).text
        return render_template("result.html", res=res)

@app.route("/dream")
def dream():
        return render_template("dream.html")        

@app.route("/dream2")
def randomgame():
        dream ={
                 "황민현":"http://imgnews.naver.net/image/433/2019/04/30/0000057840_001_20190430085734837.jpg",
                 "이태일":"http://imgnews.naver.net/image/5191/2017/11/10/0000259547_001_20171110162305769.jpg",
                 "셔누":"http://blogfiles.naver.net/MjAxNjEyMTVfNTQg/MDAxNDgxNzc1MTgzMzU4.wSP85dCXePMTWXgsCJJBhuZlVhCFHJYYQ-aWP5AbbS8g.CQVLnRsfNc-fdFIHNK14c9dY3xpE3IX1wwlXgmsLHHQg.JPEG.bluedar_fs/95CD3B88-139A-4D67-992F-F5717CE277CB.jpg",
                 "태민":"http://imgnews.naver.net/image/5645/2019/05/19/2019051909335801709482b2d760618310114012_20190519093637673.jpg",
                 "뷔":"http://imgnews.naver.net/image/022/2019/06/24/20190624504246_20190624112609600.jpg",
        }
        dream_list=list(dream.keys())
        pick = random.choice(dream_list)
        img=dream[pick]

        return render_template("dream2.html", pick =pick, img=img)

@app.route('/lotto')
def lotto():
        return render_template("lotto.html")

@app.route('/lotto_result')
def lotto_result():
        # 사용자가 입력한 정보를 가져오기
        numbers = request.args.get('numbers').split()
        user_numbers = []
        for n in numbers:
                user_numbers.append(int(n))


        #로또 홈페이지에서 정보를 가져오기
        url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
        res = requests.get(url)
        lotto_numbers = res.json()
        
        winning_numbers= []
        for i in range(1,7):
                winning_numbers.append(lotto_numbers[f'drwtNo{i}'])
        bonus_number = lotto_numbers["bnusNo"]

        result = "1등"

        matched = len(set(user_numbers) & set(winning_numbers))
        if (matched) ==6:
                result = "1등"
        elif (matched) ==5:
                result = "3등"
        elif (matched) ==4:
                result = "4등"
        elif (matched) ==3:
                result = "5등"
        else:
                result ="꽝"
        return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, b=bonus_number, r=result)



if __name__=='__main__':
   app.run(debug=True)