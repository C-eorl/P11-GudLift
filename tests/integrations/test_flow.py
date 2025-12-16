import server

class TestFlow:
    def test_booking_flow(self, client, setup_test_data):
        """
        Test booking places in competition
        1- Access connexion page
        2- login via email (john@simplylift.co)
        3- Access summary page
        4- Access booking page for "Spring Festival", places = 25
        5- Return summary page with update data
        """

        # 1
        response = client.get('/')
        assert response.status_code == 200
        assert response.request.path == '/'
        # 2 & 3
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200
        assert 'Vous êtes connecté au club Simply Lift' in response.data.decode('utf-8')
        assert response.request.path == '/showSummary'
        # 4
        response = client.post(
            '/purchasePlaces',
            data={
                'club': 'Simply Lift',
                'competition': 'Spring Festival',
                'places': 5
            },
            follow_redirects=True
        )
        assert response.status_code == 200
        assert response.request.path == '/purchasePlaces'
        assert 'Réservation réussie' in response.data.decode('utf-8')
        # 5
        club = [club for club in server.clubs if club['name'] == 'Simply Lift']
        competition = [competition for competition in server.competitions if competition['name'] == 'Spring Festival']
        assert club[0]['points'] == "8"
        assert competition[0]['numberOfPlaces'] == "20"