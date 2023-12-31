from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

def knn_get_level(github_name, k):
    model = KNeighborsClassifier(k)
    features = ['Organizations Count', 'Followers', 'Repositories Count', 'Projects Count', 'Stars',
                'Forks', 'Languages Count', 'Repositories for 3 Languages', 'Registered Days', 'Contributions']
    to_predict = 'Level'

    # create train data
    if k == 5:
        df_J = pd.read_csv('input_data\synthetic_data_Junior.csv')
        df_M = pd.read_csv('input_data\synthetic_data_Middle.csv')
        df_S = pd.read_csv('input_data\synthetic_data_Senior.csv')
        train = pd.concat([df_J, df_M, df_S], ignore_index=True, sort=False)
    elif k == 3:
        train = pd.read_csv('input_data\preprocessed_dataset.csv')

    x_train = train[features]
    y_train = train[to_predict]
    model.fit(x_train, y_train)
    y_pred = model.predict(github_name)
    return str(y_pred[0])
