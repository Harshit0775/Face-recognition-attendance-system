import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-b6d8c-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Manish Sharma",
            "major": "Civil",
            "starting_year": 2019,
            "total_attendance":6,
            "standings": "G",
            "year":4,
            "last_attendance_time": "2023-01-11 00:54:34"

        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2018,
            "total_attendance":12,
            "standings": "B",
            "year":2,
            "last_attendance_time": "2023-01-11 00:54:34"

        },
    "963852":
        {
            "name": "Elon Mus;",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance":7,
            "standings": "G",
            "year":3,
            "last_attendance_time": "2023-01-11 00:54:34"

        }

}

for key,value in data.items():
    ref.child(key).set(value)
