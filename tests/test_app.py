# tests/test_app.py

from src.opensource.app import app


def test_hello_world():
    with app.test_client() as client:
        # test_client function is provided by Flask
        response = client.get("/")
        assert response.data == b"Hello, World!"
        assert response.status_code == 200


# def test_123():
#     assert 123 == 234
