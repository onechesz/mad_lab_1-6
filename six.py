import random
import pandas


def sixth_task(dataset):
    random.seed(11)

    n = dataset.shape[0]
    m = dataset.shape[1]
    k = 100

    for l in range(k):
        i = random.randint(0, n - 1)
        j = random.randint(1, m - 1)
        dataset.iloc[i, j] = None

    nan_age = dataset[dataset['age'].isnull()].index
    data_group_g3 = dataset.groupby('G3')
    dataset['age'][nan_age] = data_group_g3['age'].mean()[dataset['G3'][nan_age]]

    for column in dataset.columns:
        nans = dataset[dataset[column].isnull()].index

        if not nans.empty:
            if dataset[column].dtype == object:
                dataset[column][nans] = dataset[column].value_counts().index.tolist()[0]
            elif column != 'G3':
                dataset[column][nans] = data_group_g3[column].mean()[dataset['G3'][nans]]

    nan_g3 = dataset[dataset['G3'].isnull()].index
    data_group_g2 = dataset.groupby('G2')
    dataset['G3'][nan_g3] = data_group_g2['G3'].mean()[dataset['G2'][nan_g3]]

    nan_freetime = dataset[dataset['freetime'].isnull()].index
    dataset['freetime'][nan_freetime] = data_group_g2['freetime'].mean()[dataset['G2'][nan_freetime]]

    return dataset.isnull().any().any()
