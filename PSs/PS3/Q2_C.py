from scipy import zscore
import numpy as np


def get_outliers(df, threshold=3):
    df['z_score'] = zscore(df['value'])
    df['is_outlier'] = np.abs(df['z_score']) > threshold
    outliers = df[df['is_outlier']]
    return outliers