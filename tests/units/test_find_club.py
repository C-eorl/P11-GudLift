import server

def test_find_club_found(monkeypatch, setup_test_data):
    club = server.find_club('Simply Lift')

    assert club == {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        }

def test_find_club_not_found(monkeypatch, setup_test_data):
    club = server.find_club('Not Found Club')

    assert club is None