from dash import callback, Input, Output

from utils.build_fig import build_fig
from utils.data_loader import load_data


@callback(
    Output('main-graph', 'figure'),
    [Input('olympiad-type-dropdown', 'value'),
     Input('year-dropdown', 'value'),
     Input('grade-dropdown', 'value')]
)
def update_graph(olympiad_type, year, grade):
    return build_fig(
        df=load_data(olympiad_type, year, grade),
        title=f"{olympiad_type} {year} ({grade} класс)"
    )
