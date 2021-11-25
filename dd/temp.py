# import pyrebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("dd/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


docs = db.collection('users').get()
for doc in docs:
                    global currUser
                    currUser = doc.id
                    global dictt
                    dictt = db.collection('users').document(currUser).get().to_dict()
print()
db.collection("users").document(currUser).update(dictt)

# # config = {
# #   "apiKey": "AIzaSyCIRFtIBHiFFw86-Eyqc3qj4Sr412Hz6rk",
# #   "authDomain": "resume-generator-2ac27.firebaseapp.com",
# #   "projectId": "resume-generator-2ac27",
# #   "storageBucket": "resume-generator-2ac27.appspot.com",
# #   "messagingSenderId": "321515779274",
# #   "appId": "1:321515779274:web:d3eff45ffed371796e7033",
# #   "databaseURL": ""
# # }   
# # firebase = pyrebase.initialize_app(config)
# # db = firebase.database()
# # all_users = db.child("users").get()
# # for user in all_users.each():
# #     print(user.val())
