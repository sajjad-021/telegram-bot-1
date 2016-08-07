# -*- coding: utf-8 -*-


def main(tg):
    tg.send_chat_action('typing')
    first_name = tg.get_me['result']['first_name']
    message = "Hi, I'm {}! A multipurpose telegram bot. You can see a list of my commands using " \
              "/help. You can also view my Admin <a href='https://telegram.me/My_Mohammad'>here Admin</a>" \
        .format(first_name)
    if 'new_chat_participant' in tg.message:
        tg.send_message(message, disable_web_page_preview=True, reply_to_message_id=None)
    else:
        tg.send_message(message, disable_web_page_preview=True)


parameters = {'name': "Start", 'short_description': "Introduces the bot!", 'permissions': True}

arguments = {'text': ["^/start$"]}
