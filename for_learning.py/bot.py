import requests
import time
from config import settings

CAT_API_URL = 'https://api.thecatapi.com/v1/images/search/'
API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = settings.tg_bot.token
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    cat_api_response = requests.get(f'{CAT_API_URL}').json()
    
    while not updates['result']:
        time.sleep(1)
        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    for result in updates['result']:
        offset = result['update_id']
        chat_id = result['message']['from']['id']
        # text = result['message']['text']
        # message = f"Your message is '{text}'"
        if cat_api_response:
            cat_pic_url = cat_api_response[0]['url']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_pic_url}')
        else:
            message = "Здесь должна была быть картинка с котом"
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={message}')

    time.sleep(1)
    counter += 1