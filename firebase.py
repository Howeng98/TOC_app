#example code for accessing Firebase
#https://bit.ly/344BUcF
#https://bit.ly/2LsrJYP
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('serviceAccount.json')

firebase_admin.initialize_app(cred)

db = firestore.client()


#-----add data to database-----
# doc_ref = db.collection("Foodlist").document("fried_rice")
# data = {
#   'name': "fried_rice",
#   'value': "3"
# }
# doc_ref.set(data)


#-----read one data-----
# doc_ref = db.collection("Foodlist").document("港式燒臘")
# docs = doc_ref.get()
#---read one data---
# print('data => {}'.format(docs.to_dict()))
# print('data => {}'.format(docs.to_dict()['價格']))

#---read all data---
# doc_ref = db.collection("Foodlist")
# docs = doc_ref.get()
# for data in docs:
#     cost = data.to_dict()['價格']
#     if cost < 100:
#         name = data.to_dict()['名字']
#         print(name,":",cost)


#-----delete data-----
# doc_ref = db.collection("Foodlist").document("food2")
# doc_ref.delete()