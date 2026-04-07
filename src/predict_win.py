import joblib
model = joblib.load("win_model.pkl")

def predict_win_probability(down, yards_to_go, yard_line, time_remaining, score_diff, score_time_iteraction):

    input_data = [[
        down,
        yards_to_go,
        yard_line,
        time_remaining,
        score_diff,
        score_time_iteraction
    ]]
    
    probability = model.predict(input_data)[0]
    probability = max(0, min(1, probability))  # Ensure probability is between 0 and 1

    return probability

# score_time_interaction = score_diff * time_remaining
