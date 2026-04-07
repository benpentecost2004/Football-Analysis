import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib

# 1. Load the data
df = pd.read_csv("4th_down_model_data_cleaned.csv", low_memory=False)

# 2. (Optional but Recommended) Filter for modern seasons if you still have the 'season' column.
# If you dropped 'season' previously, you may want to re-run your initial download script
# to keep 'season', then apply this filter:
if 'season' in df.columns:
    df = df[df['season'] >= 2018].copy()
    df = df.drop('season', axis=1) # Drop before training so it doesn't skew feature importance

# 3. Prepare Features and Target
X = df.drop("went_for_it", axis=1)
y = df["went_for_it"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)

# 4. Swap Logistic Regression for Random Forest
# Random Forest will naturally learn the complex interactions between score, time, and field position
model = RandomForestClassifier(
    n_estimators=100,       # Number of trees
    max_depth=8,            # Limit depth to prevent overfitting
    min_samples_split=10,   # Require at least 10 plays to create a new rule branch
    random_state=15,
    n_jobs=-1               # Use all CPU cores for faster training
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# 5. Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")
print(f"ROC AUC Score: {roc_auc_score(y_test, y_prob):.4f}")

joblib.dump(model, "4th_down_model.pkl")
