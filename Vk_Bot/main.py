import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='65881ca9a769a61d2edf8b59130e0cc0e757955a5ed4ac46cfff5974564e78f04e6d001f9ff797390456c')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

        if event.text == 'Соси хуй' or event.text == 'Пидр':  # Если написали заданную фразу

            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=random.randint(1, 280000),
                    message='Сам соси хуй'
                )

            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=random.randint(1, 280000),
                    message='Сам пидр'
                )

        if event.attachments == 'dock.docx':
            vk.dock.save



