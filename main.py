import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebaseKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add Data to Cloud
doc = db.collection('Heroes').document('Ironman')
doc.set({
    'name': 'Tony Stark',
    'power': 'Rich',
    'popularity': 10,
    'isJoinCivilWar': True
})

spidy = {
    'name': 'Peter Parker',
    'power': 'Spider like power',
    'popularity': 5,
    'isJoinCivilWar': True
}

doc = db.collection('Heroes').document('Spiderman')
doc.set(spidy)