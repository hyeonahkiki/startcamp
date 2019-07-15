import requests
from decouple import config
token = config("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{token}/" #/끝난걸 잘봐야함


user_id = config("CHAT_ID")

#send_url = f"{url}sendMessage?chat_id={user_id}&text=안뇨오옹"
#requests.get(send_url)
ngrok_url = "https://kkongchappy.pythonanywhere.com"
webhook_url = f"{url}setWebhook?url={ngrok_url}/{token}"
print(webhook_url)