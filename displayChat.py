import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

cred = credentials.Certificate('firebaseKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

chats = db.collection('ChatLog').document('Ada').collection('messages')

while True:
    texts = chats.stream()
    for t in texts:
        msg = t.to_dict()
        print(f'Ada says: {msg["text"]}')
    time.sleep(2)