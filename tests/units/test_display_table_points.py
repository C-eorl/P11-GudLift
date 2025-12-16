import server


def test_display_points(client, setup_test_data):
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