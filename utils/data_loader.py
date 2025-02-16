import pandas as pd


def load_point_data(
        olympiad_type: str,
        year: int = 2023,
        grade: int = 11,
) -> pd.DataFrame:
    path = f"data/points/{olympiad_type}/{year}.csv"
    df = pd.read_csv(path, sep='\t')

    return df[df['Класс участия'] == grade]


def load_point_history_data(
        olympiad_type: str,
        grade: int = 11,
) -> pd.DataFrame:
    path = f"data/points_history/{olympiad_type}.csv"
    df = pd.read_csv(path, sep=', ', engine='python')

    return df[df['class'] == grade]


def get_point_by_year(
        olympiad_type: str,
        year: int,
        grade: int,
) -> int | None:
    point_history = load_point_history_data(olympiad_type, grade)
    point = point_history[point_history['year'] == year].point

    return int(point.iloc[0]) if point.shape[0] > 0 else None
