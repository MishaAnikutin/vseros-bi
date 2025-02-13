from dash import dcc


FiltersComponent = (
    dcc.Dropdown(
        id='olympiad-type-dropdown',
        options=[
            {'label': 'Регион', 'value': 'РЭ ВОШ'},
            {'label': 'Сибириада', 'value': 'Сибириада'},
            {'label': 'Высшая проба', 'value': 'ВП'},
        ],
        value='РЭ ВОШ',
        className='dropdown'
    ),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(y), 'value': y} for y in range(2017, 2026)],
        value=2023,
        className='dropdown'
    ),
    dcc.Dropdown(
        id='grade-dropdown',
        options=[{'label': f'{g} класс', 'value': g} for g in [9, 10, 11]],
        value=11,
        className='dropdown'
    )
)