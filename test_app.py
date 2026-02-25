from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"\xc2\xa1Hola, CI/CD con DevOps!"