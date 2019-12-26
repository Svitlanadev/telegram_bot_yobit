import requests
import misc
# import json
from yobit import get_btc
from time import sleep

token = misc.token
# print(token)
# https://api.telegram.org/bot972014180:AAFQSMYZ727PBoQEiWy51wkgh1oLHtxcfmo/getUpdates
URL = 'https://api.telegram.org/bot' + token + '/'
# print(URL)

global last_udate_id
last_udate_id = 0

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def get_message():
    # erl = URL + 'sendMessage?' + 'chat_id'
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_udate_id
    if last_udate_id != current_update_id:
        last_udate_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {'chat_id':chat_id,
                   'text': message_text}
        return message
    return None


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # d = get_updates()

    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)

    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue

        sleep(2)


    # send_message(chat_id, 'What to prefere to eat this evening?')


if __name__ == '__main__':
    main()

