from dash import dcc, html


FiltersComponent = html.Div([
    dcc.Dropdown(
        id='olympiad-type-dropdown',
        options=[
            {'label': 'Региональный этап', 'value': 'region'},
            {'label': 'Заключительный этап', 'value': 'vseros'},
            {'label': 'Сибириада', 'value': 'sibiriada'},
            {'label': 'Высшая проба', 'value': 'vp'},
            {'label': 'Миссия выполнима', 'value': 'finashka'},
            {'label': 'МОШ', 'value': 'mosh'},
        ],
        value='region',
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
])
