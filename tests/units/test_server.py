import server

class TestShowSummary:
    """Test connexion & display Show competition"""

    def test_valid_mail(self, client, setup_test_data):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})

        assert response.status_code == 200
        assert 'Vous êtes connecté au club Simply Lift' in response.data.decode('utf-8')

    def test_invalid_mail(self, client, setup_test_data):
        response = client.post('/showSummary', data={'email': 'invalid@mail.com'}, follow_redirects=True)

        assert 'Aucun compte lié à cette adresse mail' in response.data.decode('utf-8')
        assert response.request.path == '/'

    def test_summary(self, client, setup_test_data):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})

        assert response.request.path == '/showSummary'


class TestPurchasePlaces:
    """Test for validation places input"""

    def test_places_more_12(self, client, setup_test_data):
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

    def test_places_0_or_less(self, client, setup_test_data):
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

    def test_available_places(self, client, setup_test_data):
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

    def test_unavailable_places(self, client, setup_test_data):
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

    def test_available_points(self, client, setup_test_data):
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

    def test_unavailable_points(self, client, setup_test_data):
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

    def test_invalid_input(self, client, setup_test_data):
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


class TestDeduce:

    def test_deduce_points(self, client, setup_test_data):
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

    def test_deduce_places(self, client, setup_test_data):
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


class TestDisplayPoints:
    def test_display_points(self, client, setup_test_data):
        """Test display points """
        response = client.get('/points')
        html = response.data.decode('utf-8')

        assert response.status_code == 200
        assert response.request.path == '/points'

        tr_count = html.count('<tr') - 1
        assert tr_count == len(server.clubs)

        for club in server.clubs:
            assert f"<td>{club['name']}</td>" in html
            assert f"<td>{club['points']}</td>" in html