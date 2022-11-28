import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCCrExzPjoIkeFMscZcL3jh5mbhkCR7lS0",
    "authDomain": "nalaiyathiran-71320.firebaseapp.com",
    "databaseURL": "https://nalaiyathiran-71320-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "nalaiyathiran-71320",
    "storageBucket": "nalaiyathiran-71320.appspot.com",
    "messagingSenderId": "811768493085",
    "appId": "1:811768493085:web:85bee3176c6b027fb7c2f4",
    "measurementId": "G-XKE62N9EJ7"
}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
