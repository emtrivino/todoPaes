from fastapi.testclient import TestClient
from app.main import app

def test_register_login():
 c=TestClient(app)
 c.post('/api/v1/auth/register',json={'email':'a@a.com','full_name':'A','password':'123456'})
 r=c.post('/api/v1/auth/login',json={'email':'a@a.com','password':'123456'})
 assert r.status_code==200 and 'access_token' in r.json()
