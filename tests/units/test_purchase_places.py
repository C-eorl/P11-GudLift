def test_places_more_12(client, setup_test_data):
    response = client.post(
        '/purchasePlaces',
        data={
            'club' : 'Simply Lift',
            'competition' : 'Spring Festival',
            'places' : 13
        },
        follow_redirects=True
    )

    assert response.request.path == '/purchasePlaces'
    assert 'Vous ne pouvez pas réserver plus de 12 places' in response.data.decode('utf-8')
    assert response.status_code == 200

def test_places_0_or_less(client, setup_test_data):
    response = client.post(
        '/purchasePlaces',
        data={
            'club' : 'Simply Lift',
            'competition' : 'Spring Festival',
            'places' : 0
        },
        follow_redirects=True
    )

    assert response.request.path == '/purchasePlaces'
    assert 'Veuillez rentrer un nombre de place positif' in response.data.decode('utf-8')
    assert response.status_code == 200

def test_available_places(client, setup_test_data):
    """SimplyLift has 13 points and Spring Festival has 25 places"""
    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Simply Lift',
            'competition': 'Spring Festival',
            'places': 5
        },
        follow_redirects=True
    )

    assert response.request.path == '/purchasePlaces'
    assert 'Réservation réussie' in response.data.decode('utf-8')

def test_unavailable_places(client, setup_test_data):
    """SimplyLift has 13 points and Test Competition has 4 places"""

    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Simply Lift',
            'competition': 'Test Competition',
            'places': 8
        },
        follow_redirects=True
    )

    assert response.request.path == '/purchasePlaces'
    assert "Il n&#39;a pas assez de place" in response.data.decode('utf-8')

def test_available_points(client, setup_test_data):
    """Another Club has 5 points """
    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Another Club',
            'competition': 'Spring Festival',
            'places': 4
        },
        follow_redirects=True
    )

    assert 'Réservation réussie' in response.data.decode('utf-8')
    assert response.request.path == '/purchasePlaces'

def test_unavailable_points(client, setup_test_data):
    """Another Club has 5 points """
    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Another Club',
            'competition': 'Spring Festival',
            'places': 10
        },
        follow_redirects=True
    )

    assert response.request.path == '/purchasePlaces'
    assert "Vous n&#39;avez pas assez de points" in response.data.decode('utf-8')

def test_invalid_input(client, setup_test_data):
    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Simply Lift',
            'competition': 'Spring Festival',
            'places': 'abc'
        },
        follow_redirects=True
    )

    assert 'Veuillez rentrer un nombre' in response.data.decode('utf-8')

