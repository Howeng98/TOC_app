from transitions.extensions import GraphMachine
from utils import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from random import randrange
import sys
wut_url = "https://i.imgur.com/TP0cynx.png"
decide = ['','',0,'','']

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)   

    #---------------------------State Condition--------------------------------#
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
        decide[0] = "早餐"
        return event.message.text.lower() == "早餐"
    
    def is_going_to_lunch(self, event):
        decide[0] = "午餐"
        return event.message.text.lower() == "午餐"
    
    def is_going_to_dinner(self, event):
        decide[0] = "晚餐"
        return event.message.text.lower() == "晚餐"

    def is_going_to_new_flavor(self, event):
        decide[1] = "試試新口味"
        return event.message.text.lower() == "試試新口味"

    def is_going_to_favorite(self, event):
        decide[1] = "最愛"
        return event.message.text.lower() == "最愛"

    def is_going_to_database(self, event):
        return event.message.text.lower() == "資料庫"
    
    def is_going_to_addData(self, event):
        return event.message.text.lower() == "新增資料"

    def is_going_to_delData(self, event):
        return event.message.text.lower() == "刪除資料"

    def is_going_to_updData(self, event):
        return event.message.text.lower() == "更新資料"

    def is_going_to_cost(self, event):
        return event.message.text.lower() == "價位"        
 
    def is_going_to_foodlist(self, event):
        text = event.message.text.lower()
        if text == "八十元以內":
            decide[2] = 1
            return True
        if text == "八十元以上一百五十元以內":
            decide[2] = 2
            return True
        if text == "一百五十元以上":
            decide[2] = 3
            return True
        if text == "美食列表":
            return True
        return False
    
    def is_going_to_random(self, event):
        return event.message.text.lower() == "隨機"    
    
    def is_going_to_end(self, event):        
        return event.message.text.lower() == "確定"
        
    def is_going_to_lobby(self, event):
        decide[0] = ""
        decide[1] = ""
        decide[2] = 0        
        return event.message.text.lower() == "返回大廳"
    
    
    

    #-----------------------------State Function---------------------------------#
    def on_enter_start(self, event):
        print("This is start section!")
        reply_token = event.reply_token
        user_id = event.source.user_id
        send_text_message(reply_token, "歡迎使用到底吃什麼App!,請根據需求點選選項～")
        btn = [
            PostbackAction(label="早餐",data="breakfast",text="早餐"),
            PostbackAction(label="午餐",data="lunch",text="午餐"),
            PostbackAction(label="晚餐",data="dinner",text="晚餐")
        ]
        button_template_send_message(user_id,"你現在要吃什麼",btn)
        return


    def on_enter_lobby(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "返回大廳")    
        return
        

    def on_enter_breakfast(self, event):
        print("早餐界面")        
        #reply_token = event.reply_token
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="試試新口味",data="trynew",text="試試新口味"),
            PostbackAction(label="最愛",data="favorite",text="最愛"),
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"對於您的早餐，您要...",btn)
        return

    def on_enter_lunch(self, event):
        print("午餐界面")
        #reply_token = event.reply_token
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="試試新口味",data="trynew",text="試試新口味"),
            PostbackAction(label="最愛",data="favorite",text="最愛"),
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"對於您的午餐，您要...",btn)
        return

    def on_enter_dinner(self, event):
        print("晚餐界面")
        #reply_token = event.reply_token
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="試試新口味",data="trynew",text="試試新口味"),
            PostbackAction(label="最愛",data="favorite",text="最愛"),
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"對於您的晚餐，您要...",btn)
        return

    def on_enter_new_flavor(self, event):
        print("試試新口味")
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="價位",data="cost",text="價位"),
            PostbackAction(label="隨機",data="random",text="隨機"),
            PostbackAction(label="美食列表",data="foodlist",text="美食列表"),            
            #PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"對於新口味，您要選擇...",btn)
        return
        
    def on_enter_favorite(self, event):
        print("最愛")
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="價位",data="cost",text="價位"),
            PostbackAction(label="隨機",data="random",text="隨機"),            
            PostbackAction(label="美食列表",data="foodlist",text="美食列表"),
            PostbackAction(label="資料庫",data="adddata",text="資料庫"),            
            #PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"對於您的最愛，您要...",btn)
        return

    def on_enter_database(self, event):
        print("資料庫")
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="新增資料",data="adddata",text="新增資料"),
            PostbackAction(label="刪除資料",data="deldata",text="刪除資料"),            
            PostbackAction(label="更新資料",data="upddata",text="更新資料"),                       
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"對於資料庫，您要...",btn)
        return

    def on_enter_addData(self, event):
        print("增加新資料")
        user_id = event.source.user_id        
        doc_ref = db.collection("Favorite","美食菜單","早餐").document("快樂薯條")               
        data = {
            '價格': 90,
            '名字': "快樂薯條"            
        }
        doc_ref.set(data)        
        btn = [
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"資料新增成功!",btn)
        return

    def on_enter_delData(self, event):
        print("刪除資料")
        user_id = event.source.user_id 
        doc_ref = db.collection("Favorite","美食菜單","早餐").document("快樂薯條")
        doc_ref.delete()
        btn = [
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"資料刪除成功!",btn)
        return

    def on_enter_updData(self, event):
        print("更新資料")
        user_id = event.source.user_id 
        doc_ref = db.collection("Favorite","美食菜單","早餐").document("快樂薯條")
        doc_ref.update({
            '價格': 999,
            '名字':"傷心薯條",
        })
        btn = [
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"資料更新成功!",btn)
        return

    def on_enter_cost(self, event):
        print("價位")
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="八十元以內",data="less than 100",text="八十元以內"),
            PostbackAction(label="八十元以上一百五十元以內",data="greater than 80 and less than 150",text="八十元以上一百五十元以內"),
            PostbackAction(label="一百五十元以上",data="greater than 150",text="一百五十元以上"),            
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        button_template_send_message(user_id,"對於價格的部分，你打算選擇...",btn)
        return

    def on_enter_foodlist(self, event):
        print("美食列表")
        send_text_message(event.reply_token, "以下是我們所推薦的美食列表\n您打算選擇...")        
        user_id = event.source.user_id
        doc_ref = db.collection("Foodlist","美食菜單","午餐")
        if decide[0] == "早餐" and decide[1] == "試試新口味":
            doc_ref = db.collection("Foodlist","美食菜單","早餐")
        if decide[0] == "午餐" and decide[1] == "試試新口味":
            doc_ref = db.collection("Foodlist","美食菜單","午餐")
        if decide[0] == "晚餐" and decide[1] == "試試新口味":
            doc_ref = db.collection("Foodlist","美食菜單","晚餐")
        if decide[0] == "早餐" and decide[1] == "最愛":
            doc_ref = db.collection("Favorite","美食菜單","早餐")
        if decide[0] == "午餐" and decide[1] == "最愛":
            doc_ref = db.collection("Favorite","美食菜單","午餐")
        if decide[0] == "晚餐" and decide[1] == "最愛":
            doc_ref = db.collection("Favorite","美食菜單","晚餐")                  
        docs = doc_ref.get()
        btn = [
            PostbackAction(label="確定",data="ok",text="確定"),
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        exit_btn = [
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]              
        gotFood = 0                    
        for data in docs:
            cost = data.to_dict()['價格']
            if decide[2] == 0:
                labelName = data.to_dict()['名字']
                labelName = labelName + ":" + str(cost)
                button_template_send_message(user_id,labelName,btn)

            if decide[2] == 1:
                if cost <= 80:                
                    gotFood = 1
                    labelName = data.to_dict()['名字']
                    labelName = labelName + ":" + str(cost)
                    button_template_send_message(user_id,labelName,btn)              
                elif gotFood == 0:
                    button_template_send_message(user_id,"抱歉！沒有符合條件的美食QQ",exit_btn)
                    return
            if decide[2] == 2:
                if cost > 80 and cost <= 150:     
                    gotFood = 1           
                    labelName = data.to_dict()['名字']
                    labelName = labelName + ":" + str(cost)
                    button_template_send_message(user_id,labelName,btn)   
                elif gotFood == 0:
                    button_template_send_message(user_id,"抱歉！沒有符合條件的美食QQ",exit_btn)
                    returnurl
            if decide[2] == 3:
                if cost > 150:             
                    gotFood = 1   
                    labelName = data.to_dict()['名字']
                    labelName = labelName + ":" + str(cost)
                    button_template_send_message(user_id,labelName,btn)   
                elif gotFood == 0:
                    button_template_send_message(user_id,"抱歉！沒有符合條件的美食QQ",exit_btn)
                    return
        return

    def on_enter_random(self, event):
        print("隨機")
        send_text_message(event.reply_token, "吃什麼？隨便啦!!!煩餒...")                
        user_id = event.source.user_id
        if decide[0] == "早餐" and decide[1] == "試試新口味":
            doc_ref = db.collection("Foodlist","美食菜單","早餐")
        if decide[0] == "午餐" and decide[1] == "試試新口味":
            doc_ref = db.collection("Foodlist","美食菜單","午餐")
        if decide[0] == "晚餐" and decide[1] == "試試新口味":
            doc_ref = db.collection("Foodlist","美食菜單","晚餐")
        if decide[0] == "早餐" and decide[1] == "最愛":
            doc_ref = db.collection("Favorite","美食菜單","早餐")
        if decide[0] == "午餐" and decide[1] == "最愛":
            doc_ref = db.collection("Favorite","美食菜單","午餐")
        if decide[0] == "晚餐" and decide[1] == "最愛":
            doc_ref = db.collection("Favorite","美食菜單","晚餐")                    
        docs = doc_ref.get()
        btn = [
            PostbackAction(label="確定",data="ok",text="確定"),
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]
        exit_btn = [
            PostbackAction(label="返回大廳",data="go_back",text="返回大廳")
        ]     
        counter = 0
        length = 0
        num = 0
        # for data in docs:
        #     length+=1 
        length = 3           
        for data in docs:
            cost = data.to_dict()['價格']
            if length != 0:
                counter += 1
                num = randrange(1,length)
                if num == counter:
                    labelName = data.to_dict()['名字']
                    labelName = labelName + ":" + str(cost)
                    button_template_send_message(user_id,labelName,btn)
                    return
                return                                
            else:
                button_template_send_message(user_id,"抱歉!美食名單是空的～",exit_btn)
                return   
        return    
        
    def on_enter_end(self, event):
        print("確定")
        user_id = event.source.user_id
        btn = [
            PostbackAction(label="返回大廳",data="ok",text="返回大廳")
           ]
        send_image_message(user_id,wut_url)                   
        button_template_send_message(user_id,"恭喜！你終於決定好要吃什麼啦！！ =.= ~",btn)
        return
        
    #---------------------------------------------------------------------------#

    
        