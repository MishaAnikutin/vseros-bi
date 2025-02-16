import pandas as pd


def get_forecast(point_data: pd.DataFrame):
    return point_data['Зачетный балл'].quantile(0.75)
