def calculate_weighted_score(scores:dict,weights:dict)->float:
 return sum(scores.get(k,0)*weights.get(k,0) for k in weights)/100
