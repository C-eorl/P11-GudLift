import server


def test_deduce_points(client, setup_test_data):
    """Test deduce point in to purchase - Simply Lift has 13 points"""
    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Simply Lift',
            'competition': 'Spring Festival',
            'places': 5
        }
    )
    club = [club for club in server.clubs if club['name'] == 'Simply Lift']
    assert club[0]['points'] == "8"

def test_deduce_places(client, setup_test_data):
    """Test deduce place in to purchase - Spring Festival has 25 places"""
    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Simply Lift',
            'competition': 'Spring Festival',
            'places': 10
        }
    )
    competition = [competition for competition in server.competitions if competition['name'] == 'Spring Festival']
    assert competition[0]['numberOfPlaces'] == "15"

