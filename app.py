import streamlit as st
from predict_4th_down import predict_go_for_it
from predict_win import predict_win_probability

st.set_page_config(page_title="Football Analysis App", page_icon="🏈", layout="centered")

st.title("Football Analysis App")

# -------------------------
# 4TH DOWN DECISION MODEL
# -------------------------

st.header("4th Down Decision Prediction")

ydstogo = st.number_input(
    "Yards to go",
    min_value=1,
    max_value=99,
    value=None,
    key="fourth_ydstogo"
)

yardline_100 = st.number_input(
    "Yard line (distance from end zone)",
    min_value=1,
    max_value=99,
    value=None,
    key="fourth_yardline"
)

time_remaining = st.number_input(
    "Time remaining (seconds)",
    min_value=0,
    max_value=3600,
    value=None,
    key="fourth_time"
)

score_diff = st.number_input(
    "Score difference (negative if trailing)",
    min_value=-100,
    max_value=100,
    value=None,
    key="fourth_score"
)

qtr = st.number_input(
    "Quarter",
    min_value=1,
    max_value=4,
    value=None,
    key="fourth_qtr"
)

if st.button("Predict 4th Down Decision"):

    if None in (ydstogo, yardline_100, time_remaining, score_diff, qtr):
        st.warning("Please fill in all fields.")
    else:
        result = predict_go_for_it(
            ydstogo,
            yardline_100,
            time_remaining,
            score_diff,
            qtr
        )

        st.write(f"Predicted Decision: {result}")


# -------------------------
# WIN PROBABILITY MODEL
# -------------------------

st.header("Win Probability Prediction")

down = st.number_input(
    "Down",
    min_value=1,
    max_value=4,
    value=None,
    key="win_down"
)

yards_to_go = st.number_input(
    "Yards to go",
    min_value=1,
    max_value=99,
    value=None,
    key="win_ydstogo"
)

yard_line = st.number_input(
    "Yard line (distance from end zone)",
    min_value=1,
    max_value=99,
    value=None,
    key="win_yardline"
)

time_remaining_win = st.number_input(
    "Time remaining (seconds)",
    min_value=0,
    max_value=3600,
    value=None,
    key="win_time"
)

score_diff_win = st.number_input(
    "Score difference (negative if trailing)",
    min_value=-100,
    max_value=100,
    value=None,
    key="win_score"
)

if st.button("Predict Win Probability"):

    if None in (down, yards_to_go, yard_line, time_remaining_win, score_diff_win):
        st.warning("Please fill in all fields.")
    else:
        score_time_interaction = score_diff_win * time_remaining_win

        result = predict_win_probability(
            down,
            yards_to_go,
            yard_line,
            time_remaining_win,
            score_diff_win,
            score_time_interaction
        )

        st.write(f"Predicted Win Probability: {result}")
