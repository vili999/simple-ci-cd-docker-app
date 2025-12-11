from app.main import root

def test_root_message():
    assert root() == {"message": "Hello from Vili's DevOps CI/CD Project!"}
