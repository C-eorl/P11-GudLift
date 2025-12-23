import server

def test_find_competition_found(monkeypatch, setup_test_data):
    competition = server.find_competition('Spring Festival')

    assert competition == {
            "name": "Spring Festival",
            "date": "2026-03-27 10:00:00",
            "numberOfPlaces": "25"
        }

def test_find_club_not_found(monkeypatch, setup_test_data):
    competition = server.find_competition('Not Found Competition')

    assert competition is None