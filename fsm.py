from transitions.extensions import GraphMachine

from utils import *

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)   

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "go to start"

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_state３(self, event):
        text = event.message.text
        return text.lower() == "go to state3"

    def is_going_to_back(self, event):
        text = event.message.text
        return text.lower() == "go back"

    def is_going_to_breakfast(self, event):
        return event.message.text.lower() == "早餐"
    
    def is_going_to_lunch(self, event):
        return event.message.text.lower() == "午餐"
    
    def is_going_to_dinner(self, event):
        return event.message.text.lower() == "晚餐"
    
    def is_going_to_lobby(self, event):
        return event.message.text.lower() == "返回大廳"
    

    def on_enter_start(self, event):
        print("This is start section!")
        reply_token = event.reply_token
        #image_url = "https://i.imgur.com/eTldj2E.png?1"
        user_id = event.source.user_id
        send_text_message(reply_token, "歡迎使用到底吃什麼App!,請根據需求點選選項～")
        button_template_send_message(user_id)
        
    def on_enter_breakfast(self, event):
        print("早餐界面")
        #test_button_template(self)
        #user_id = event.source.user_id
        reply_token = event.reply_token
        send_text_message(reply_token, "早餐界面")
        
    def on_enter_lunch(self, event):
        print("午餐界面")
        reply_token = event.reply_token
        send_text_message(reply_token, "午餐界面")

    def on_enter_dinner(self, event):
        print("晚餐界面")
        reply_token = event.reply_token
        send_text_message(reply_token, "晚餐界面")

    def on_enter_lobby(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "返回大廳")
        