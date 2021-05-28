import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebaseKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = db.collection('ChatLog').document('Ada').collection('messages')

while True:
    text = input("Says: ")
    print("Ada says:", text)

    doc.add({
        'text': text
    })