
client = TestClient(app)


def test_api_status():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
