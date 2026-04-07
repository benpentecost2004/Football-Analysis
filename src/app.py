import streamlit as st
from predict_4th_down import predict_go_for_it
from predict_win import predict_win_probability

st.set_page_config(page_title="Football Analysis App", page_icon="🏈", layout="centered")

st.title("Football Analysis")

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
        # Unpack the two values returned by your model
        decision, probability = predict_go_for_it(
            ydstogo,
            yardline_100,
            time_remaining,
            score_diff,
            qtr
        )
        
        # Convert the decimal probability (e.g., 0.85) to a percentage (85.0)
        prob_percent = probability * 100
        
        # Display the text results
        st.write(f"**Predicted Decision:** {decision}")
        st.write(f"**Predicted Go-For-It Probability:** {prob_percent:.1f}%")

        # Determine the color based on the percentage
        if prob_percent < 20:
            bar_color = "#ff4b4b" # Red
        elif 20 <= prob_percent <= 40:
            bar_color = "#ffa500" # Orange
        elif 40 < prob_percent <= 70:
            bar_color = "#ffd700" # Yellow
        else:
            bar_color = "#00c04b" # Green
            
        # Ensure width doesn't break CSS if the model outputs slightly below 0 or above 100
        safe_width = max(0, min(prob_percent, 100))

        # Create custom HTML progress bar
        progress_html = f"""
        <div style="width: 100%; background-color: #e6e6e6; border-radius: 5px; margin-top: 10px; margin-bottom: 20px;">
          <div style="width: {safe_width}%; height: 24px; background-color: {bar_color}; border-radius: 5px; transition: width 0.5s;">
          </div>
        </div>
        """
        
        # Render the bar
        st.markdown(progress_html, unsafe_allow_html=True)

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

        # Get the result from your model
        result = predict_win_probability(
            down,
            yards_to_go,
            yard_line,
            time_remaining_win,
            score_diff_win,
            score_time_interaction
        )

        # NOTE: If your model returns a decimal (e.g., 0.75), multiply by 100. 
        # If it already returns a whole number (e.g., 75.0), you can remove the "* 100".
        win_prob_percent = result * 100 

        # Display the text result
        st.write(f"**Predicted Win Probability:** {win_prob_percent:.1f}%")

        # Determine the color based on the percentage
        if win_prob_percent < 20:
            bar_color = "#ff4b4b" # Red
        elif 20 <= win_prob_percent <= 40:
            bar_color = "#ffa500" # Orange
        elif 40 < win_prob_percent <= 70:
            bar_color = "#ffd700" # Yellow
        else:
            bar_color = "#00c04b" # Green
            
        # Ensure width doesn't break CSS if the model outputs slightly below 0 or above 100
        safe_width = max(0, min(win_prob_percent, 100))

        # Create custom HTML progress bar
        progress_html = f"""
        <div style="width: 100%; background-color: #e6e6e6; border-radius: 5px; margin-top: 10px; margin-bottom: 20px;">
          <div style="width: {safe_width}%; height: 24px; background-color: {bar_color}; border-radius: 5px; transition: width 0.5s;">
          </div>
        </div>
        """
        
        # Render the bar
        st.markdown(progress_html, unsafe_allow_html=True)