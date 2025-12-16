
clubs = [
        {
            "name": "Test Club",
            "email": "test@club.com",
            "points": "10"
        },
        {
            "name": "Another Club",
            "email": "another@club.com",
            "points": "5"
        },
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]

name = "kate@shelifts.co.uk"

def find_club(club_name):
    for club in clubs:
        if club_name in club.values():
            return club
    return None

print(f"fonction: {find_club(name)}")
