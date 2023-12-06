def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    best_v = 0
    best_k = None
    for key, value in a_dictionary.items():
        if value >= best_v:
            best_v = value
            best_k = key
    return (best_k)
