import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='12153e7f74d0c0257192e7f5b525f894cfd507168976a15b0d3490235ff76bd85b2a6fa05b42f9cd6737b')

longPoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longPoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        atchs = event.object['attachments']

        if atchs:
            for atch in atchs:
                if atch['type'] == 'dod':
                    document = atch['doc']




# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
#         if event.text == 'Соси хуй' or event.text == 'Пидр':
#             if event.from_user:
#                 vk.messages.send(
#                     user_id=event.user_id,
#                     random_id=random.randint(1, 280000),
#                     message='Сам соси хуй'
#                 )
#
#             elif event.from_chat:
#                 vk.messages.send(
#                     chat_id=event.chat_id,
#                     random_id=random.randint(1, 280000),
#                     message='Сам пидр'
#                 )
#
#         if event.attachments == "dock.docx" and event.from_user:
#             vk.messages.send(
#                 user_id=event.user_id,
#                 random_id=random.randint(1, 280000),
#                 message='Сам соси хуй'
#             )
