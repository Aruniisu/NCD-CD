import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import app  # now works

def test_home():
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    assert b"Hello" in response.data
