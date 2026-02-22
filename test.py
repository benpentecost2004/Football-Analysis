import pandas as pd
df = pd.read_csv("data/data.csv", low_memory=False)

columns_needed = [
    "down",
    "ydstogo",
    "yardline_100",
    "game_seconds_remaining",
    "score_differential",
    "qtr",
    "posteam",
    "play_type",
    "wp",
    "epa"
]

df = df[columns_needed].copy()

df = df[df["down"] == 4]

df = df[df["play_type"].isin(["run", "pass", "punt", "field_goal"])]

df["go_for_it"] = df["play_type"].apply(
    lambda x: 1 if x in ["run", "pass"] else 0
)

df = df.dropna()

df.to_csv("4th_down_model_data.csv", index=False)

print("CSV successfully saved.")