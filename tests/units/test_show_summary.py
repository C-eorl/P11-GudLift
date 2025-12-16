def test_valid_mail(client, setup_test_data):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})

    assert response.status_code == 200
    assert 'Vous êtes connecté au club Simply Lift' in response.data.decode('utf-8')

def test_invalid_mail(client, setup_test_data):
    response = client.post('/showSummary', data={'email': 'invalid@mail.com'}, follow_redirects=True)

    assert 'Aucun compte lié à cette adresse mail' in response.data.decode('utf-8')
    assert response.request.path == '/'

def test_summary(client, setup_test_data):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})

    assert response.request.path == '/showSummary'
