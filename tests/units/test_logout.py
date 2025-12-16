def test_logout(client):
    """Logout page"""
    response = client.get('/logout')
    assert response.status_code == 302
    assert response.request.path == "/logout"

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == "/"