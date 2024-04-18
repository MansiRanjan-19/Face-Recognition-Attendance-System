import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' :" "
})

ref = db.reference('Students')

data = {
    "D2021":{
        "name": " ",
        "Major": "Medical",
        "Starting_year": 2021,
        "total_attendance": 20,
        "standing": "G",
        "Year": 2,
        "last_attendance_time": "2024-12-11 00:54:34"

    },
"M2025":{
        "name": " ",
        "Major": "AIML",
        "Starting_year": 2021,
        "total_attendance": 30,
        "standing": "G",
        "Year": 3,
        "last_attendance_time": "2024-04-10 00:20:31"

    },
"R2004":{
        "name": " ",
        "Major": "BCA",
        "Starting_year": 2021,
        "total_attendance": 15,
        "standing": "B",
        "Year": 2,
        "last_attendance_time": "2024-01-11 00:54:34"

    },
"R2020":{
        "name": " ",
        "Major": "Computer Science",
        "Starting_year": 2021,
        "total_attendance": 4,
        "standing": "G",
        "Year": 1,
        "last_attendance_time": "2023-12-11 00:54:34"

    },
"R2026":{
        "name": " ",
        "Major": "Medical",
        "Starting_year": 2021,
        "total_attendance": 44,
        "standing": "G",
        "Year": 2,
        "last_attendance_time": "2023-05-11 00:54:34"

    }
}

for key,value in data.items():
    ref.child(key).set(value)
