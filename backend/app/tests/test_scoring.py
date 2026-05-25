from app.services.scoring_service import estimate_paes_score

def test_scoring():
 assert estimate_paes_score(0)==100
 assert estimate_paes_score(1)==1000
