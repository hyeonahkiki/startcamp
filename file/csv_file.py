import csv

lunch = {
    "bbq":"123-123", # , 잘쓰기
    "중국집":"456-456",
    "한식":"789-789"
}

with open("lunch.csv", 'w', encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)#csv모듈을 통해 쓰는거

    for item in lunch.items():
        csv_writer.writerow(item)
