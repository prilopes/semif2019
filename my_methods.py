def bar_chart(feature, train, projection='Survived'):
    import pandas as pd
    if projection == 'Survived':
        survived = train[train['Survived'] == 1][feature].value_counts()
        dead = train[train['Survived'] == 0][feature].value_counts()
        df = pd.DataFrame([survived, dead])
        df.index = ['Sobreviveu', 'Não Sobreviveu']
    else:
        unique_proj_values = train[projection].unique()
        counts = []
        for value in unique_proj_values:
            count = train[train[projection] == value][feature].value_counts()
            counts.append(count)
        df = pd.DataFrame(counts)
        df.index = unique_proj_values

    df.plot(kind='bar', stacked=True, figsize=(10,5))


def encode_string(feature, data):
    from sklearn.preprocessing import LabelEncoder
    lb = LabelEncoder()
    return lb.fit_transform(data[feature].astype(str))