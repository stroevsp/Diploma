import vk_api
import random
import requests
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token='12153e7f74d0c0257192e7f5b525f894cfd507168976a15b0d3490235ff76bd85b2a6fa05b42f9cd6737b')

longPoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def create_keyboard(response):
    if response == 'начать':
        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button('Отправить статью', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Список команд', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Инфо', color=VkKeyboardColor.DEFAULT)

        keyboard = keyboard.get_keyboard()
        return keyboard


for event in longPoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        print('Message sent: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        response = event.text.lower()
        keyboard = create_keyboard(response)
        doc = event.attachments
        print(doc)
        print(response)

        if doc != {}:
            doc_info = vk_session.method(
                'messages.getById',
                {
                    'message_ids': event.message_id,
                }

            )
            url = doc_info['items'][0]['attachments'][0]['doc']['url']
            download = requests.get(url)
            try:
                test = download.text.encode('latin1').decode('cp1251')
                print(test)
            except:
                print('error')

        elif response == 'начать':
            vk_session.method(
                'messages.send',
                {
                    'user_id': event.user_id,
                    'message': 'Здравстуйте',
                    'random_id': random.randint(1, 2800000),
                    'keyboard': keyboard
                }
            )

        elif response == 'отправить статью':
            vk_session.method(
                'messages.send',
                {
                    'user_id': event.user_id,
                    'message': 'Скопируйте текст вашей статьи в этот диалог',
                    'random_id': random.randint(1, 2800000),
                }
            )

        else:
            vk_session.method(
                'messages.send',
                {
                    'user_id': event.user_id,
                    'message': 'Я вас не понимаю',
                    'random_id': random.randint(1, 2800000)
                }
            )
