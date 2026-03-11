import pickle
import pandas as pd

# Load model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load features
with open("model/features.pkl", "rb") as f:
    features = pickle.load(f)


def predict_risk(user_input):

    input_df = pd.DataFrame(columns=features)

    input_df.loc[0] = 0

    for key, value in user_input.items():
        if key in input_df.columns:
            input_df[key] = value

    probability = model.predict_proba(input_df)[0][1]

    return probability


def get_feature_importance():

    importance = model.feature_importances_

    feature_importance = dict(zip(features, importance))

    sorted_features = sorted(
        feature_importance.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_features[:3]