import pytest
from server import app
import server

@pytest.fixture
def client():
    """Create client for testing"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

##########################################################################
#            Fixture - competition
###########################################################################
@pytest.fixture
def sample_competitions():
    """Fixture compétitions for test"""
    return [
        {
            "name": "Test Competition",
            "date": "2026-03-27 10:00:00",
            "numberOfPlaces": "4"
        },
        {
            "name": "Spring Festival",
            "date": "2026-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2026-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Past Competition",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]


@pytest.fixture
def patched_competitions(sample_competitions, monkeypatch):
    monkeypatch.setattr(server,"competitions", sample_competitions.copy())


##########################################################################
#            Fixture - clubs
###########################################################################
@pytest.fixture
def sample_clubs():
    """Fixture clubs for test"""
    return [
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

@pytest.fixture
def patched_clubs(sample_clubs, monkeypatch):
    monkeypatch.setattr(server, "clubs", sample_clubs.copy())

###############################################################################

@pytest.fixture
def no_save(monkeypatch):
    monkeypatch.setattr(server, "save_clubs", lambda *args: None)
    monkeypatch.setattr(server, "save_competitions", lambda *args: None)

@pytest.fixture
def setup_test_data(patched_competitions, patched_clubs, no_save):
    """combined fixture for test"""
    pass