# Football Analysis Tool
## An NFL 4th Down Decision & Win Probability Model


### Project Overview

This project is a machine learning–based decision support system designed to analyze American football game situations and generate two key predictions:
	1.	4th Down Decision Probability – The probability that a team will “go for it” on 4th down rather than punt or attempt a field goal.
	2.	Win Probability Calculator – The probability that a team will win the game based on the current game state.

The model uses historical NFL play-by-play data to learn how teams behave in different game situations and to estimate winning chances given contextual variables.


### Dataset

The model is trained using historical NFL play-by-play data from the nflfastR dataset (2023 season).

Selected features include:
	•	down
	•	ydstogo
	•	yardline_100
	•	game_seconds_remaining
	•	score_differential
	•	qtr
	•	posteam
	•	play_type
	•	wp (win probability)
	•	epa (expected points added)

The dataset is filtered to:
	•	4th down situations
	•	Relevant decision plays (run, pass, punt, field goal)

A binary target variable go_for_it is created:
	•	1 → Run/Pass (attempt conversion)
	•	0 → Punt/Field Goal


### Machine Learning Approach

Model Type

The baseline implementation uses Logistic Regression, which is well-suited for binary classification and probability estimation.

Why Logistic Regression?
	•	Outputs calibrated probabilities
	•	Interpretable coefficients
	•	Strong baseline performance for decision modeling
	•	Commonly used in sports analytics


### Feature Inputs

4th Down Model Inputs
	•	Yards to go
	•	Field position (distance to end zone)
	•	Time remaining (seconds)
	•	Score differential
	•	Quarter

Win Probability Model Inputs
	•	Score differential
	•	Time remaining
	•	Quarter
	•	Field position


### How It Works
	1.	Load and clean play-by-play data
	2.	Filter to relevant game states
	3.	Create target variable
	4.	Train classification model
	5.	Use predict_proba() to generate probability outputs
	6.	Accept user input and return percentage predictions



### Application

This project demonstrates:
	•	Supervised machine learning
	•	Sports analytics modeling
	•	Probability calibration
	•	Feature engineering
	•	Real-world decision modeling

Potential real-world applications include:
	•	Coaching decision support tools
	•	Sports broadcasting analytics
	•	Fan engagement tools
	•	Betting market modeling

### Tech stack
	•	Python
	•	Pandas
	•	Scikit-learn
	•	NFL play-by-play dataset (nflfastR)
