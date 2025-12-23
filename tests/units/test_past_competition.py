def test_past_competition(client, setup_test_data):
    """SimplyLift has 13 points and Past Competition has 25 places, but she's past"""
    response = client.get(
        '/book/Past Competition/SimplyLift',
        follow_redirects=True
    )

    assert 'Impossible de réserver des places pour une compétition passée' in response.data.decode('utf-8')

def test_futur_competition(client, setup_test_data):
    """SimplyLift has 13 points and Spring Festival has 25 places,
    Spring Festival date is 2026-03-27 10:00:00 for test"""
    response = client.get(
        '/book/Spring Festival/SimplyLift',
        follow_redirects=True
    )

    assert response.request.path == "/book/Spring Festival/SimplyLift"
