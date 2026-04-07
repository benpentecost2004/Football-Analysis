import joblib
model = joblib.load("4th_down_model.pkl")

def predict_go_for_it(ydstogo, yardline_100, time_remaining, score_diff, qtr):
    
    input_data = [[
        4,                # down (always 4 for this model)
        ydstogo,
        yardline_100,
        time_remaining,
        score_diff,
        qtr
    ]]
    
    probability = model.predict_proba(input_data)[0][1]

    decision = "GO FOR IT" if probability >= 0.5 else "PUNT/KICK"

    print(f"Should the team go for it? {decision}")

    return decision, probability

