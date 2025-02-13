import pandas as pd


def load_data(
        olympiad_type: str,
        year: int = 2023,
        grade: int = 11,
) -> pd.DataFrame:
    df = pd.read_csv(
        filepath_or_buffer=f"data/{olympiad_type} экономика {year}.csv",
        sep='\t'
    )

    return df[df['Класс участия'] == grade]
