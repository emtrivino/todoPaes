from app.services.career_simulator_service import calculate_weighted_score

def test_weighted():
 assert calculate_weighted_score({'m1':700},{'m1':50})==350
