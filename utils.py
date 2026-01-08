import json

initials_clubs = {
    "clubs":[
        {
            "name":"Simply Lift",
            "email":"john@simplylift.co",
            "points":"13"
        },
        {
            "name":"Iron Temple",
            "email": "admin@irontemple.com",
            "points":"4"
        },
        {   "name":"She Lifts",
            "email": "kate@shelifts.co.uk",
            "points":"12"
        }
    ]
}
initials_competitions = {
"competitions": [
    {
        "name": "Spring Festival",
        "date": "2026-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
    {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    }
]
}

with open('clubs.json', 'w') as f:
    json.dump(initials_clubs, f, indent=4)

with open('competitions.json', 'w') as f:
    json.dump(initials_competitions, f, indent=4)

print("Données réinitialisées !")

