import vk_api
import random
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token='12153e7f74d0c0257192e7f5b525f894cfd507168976a15b0d3490235ff76bd85b2a6fa05b42f9cd6737b')

longPoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def create_keyboard(response):
    if response == 'начать':
        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button('Отправить статью', color=VkKeyboardColor.DEFAULT)
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
        print(response)
        if response == 'начать':
            vk_session.method(
                'messages.send',
                {
                    'user_id': event.user_id,
                    'message': 'Здравстуйте',
                    'random_id': random.randint(1, 2800000),
                    'keyboard': keyboard
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
