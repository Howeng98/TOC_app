import os
import json
import requests
from linebot import LineBotApi, WebhookParser
from linebot.models import *

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_text_push_msg(reply_token,text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(reply_token, TextSendMessage(text=text))


def quick_reply(id):
    line_bot_api = LineBotApi(channel_access_token)        
    textMessage = TextSendMessage(text="HelloWorld",quick_reply="Hi")
    line_bot_api.push_message(id,textMessage)


def template_send_message(id):
    line_bot_api = LineBotApi(channel_access_token)
    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='Are you sure?',
                actions=[
                    PostbackAction(
                        label='postback',
                        text='postback text',
                        data='action=buy&itemid=1',                        
                    ),
                    MessageAction(
                        label='message',
                        text='message text'
                    )
                ]
        )
    )
    line_bot_api.push_message(id,confirm_template_message)

def button_template_send_message(id,titleText,button):
    line_bot_api = LineBotApi(channel_access_token)
    button_template = ButtonsTemplate(
        title=titleText,text=' ',actions=button        
    )
    template_message = TemplateSendMessage(alt_text="請用手機看此訊息",template=button_template)
    line_bot_api.push_message(id,template_message)

def send_image_message(id,url):
    line_bot_api = LineBotApi(channel_access_token)
    message =  ImageSendMessage(        
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.push_message(id,message)


