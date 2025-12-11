from app.main import root

def test_root():
    expected = {"message": "Hello from Vili's DevOps CI/CD Project!"}
    assert root() == expected

