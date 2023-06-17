from joblib import load
import numpy as np
import pandas as pd
from User import User


def decode_levels(predicted_value):
    level_mapper = {"1": "Junior", "2": "Middle", "3": "Senior"}
    predicted_level = level_mapper[predicted_value]

    return predicted_level


def make_user_feature_vector(username, github_token):
    user = User(username, github_token=github_token)

    user_feature_dict = {
        'Organizations Count': [user.organizations_count],
        'Followers': [user.followers],
        'Repositories Count': [user.repositories_count],
        'Projects Count': [user.projects_count],
        'Stars': [user.stars],
        'Forks': [user.forks],
        'Languages Count': [user.languages_count],
        'Repositories for 3 Languages': [user.repositories_for_3_popular_languages_count],
        'Registered Days': [user.registered_days],
        'Contributions': [user.contributions],
    }

    user_feature_vector = pd.DataFrame(user_feature_dict)

    return user_feature_vector


def normalize_user_feature_vector(user_feature_vector):

    for column_name in user_feature_vector:
        scaler = load(f'scalers/{column_name}_scaler.pkl')

        data = user_feature_vector[column_name]

        normalized_data = scaler.transform(np.array(data).reshape(-1, 1))

        user_feature_vector[column_name] = normalized_data

    return user_feature_vector
