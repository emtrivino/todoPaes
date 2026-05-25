def estimate_paes_score(accuracy:float)->int:
 accuracy=max(0.0,min(1.0,accuracy))
 return round(100+900*(accuracy**0.85))
