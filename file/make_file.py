# f = open("student.txt", "w")
# f.write("안녕하세요")
# f.close()

with open("ssafy.txt", 'a') as f: #open(a, w) : a를 w로 연다 / r+: 읽다 w : 쓰다 a: 추가
    f.write("화이팅 싸피!!!???????")#f.write()전체 데이터를 덮어씌운다