Создание бота
[@BotFather](https://core.telegram.org/bots#how-do-i-create-a-bot:~:text=%D0%BD%D0%B0%D1%87%D0%B0%D1%82%D1%8C%2C%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D1%8C%D1%82%D0%B5%20%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B5-,%40BotFather,-%D0%B2%20Telegram%2C%20%D1%87%D1%82%D0%BE%D0%B1%D1%8B)

bot: [@neuralchat111_bot](t.me/neuralchat111_bot)

отправка запросов к telegram API
```python
def send_request(method, params=None):
    url = API_URL + method
    response = requests.get(url, params=params)
    return response.json()
```
проверка на новые сообщения
```python
def get_updates(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = send_request("getUpdates", params)
    return response["result"]
```
отправка сообщений пользователю
```python
def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    send_request("sendMessage", params)
```