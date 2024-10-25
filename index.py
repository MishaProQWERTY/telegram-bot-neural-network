import requests
import time

from contend import buildPhrase

TOKEN = "token_you"
API_URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_request(method, params=None):
    url = API_URL + method
    response = requests.get(url, params=params)
    return response.json()

def get_updates(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = send_request("getUpdates", params)
    return response["result"]

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    send_request("sendMessage", params)


def handle_message(chat_id, mess):
    text = str(mess)
    if text == '/start': send_message(chat_id, 'Привет! Я бот, который использует нейросеть, чтобы отвечать вам')
    else:
        try:
            output = buildPhrase(text)
        except:
            output = 'Что-то пошло не так.\nПопробуй что-то другое'

        send_message(chat_id, output)



def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")
                
                if text:
                    handle_message(chat_id, text)

                offset = update["update_id"] + 1
        
        time.sleep(1)

if __name__ == "__main__":
    main()