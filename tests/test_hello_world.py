def test_request_example(app, client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
