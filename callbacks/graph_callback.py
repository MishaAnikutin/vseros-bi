from dash import callback, Input, Output

from utils.build_fig import build_point_fig, build_point_history_fig
from utils.data_loader import load_point_data, load_point_history_data, get_point_by_year
from utils.forecast import get_forecast


@callback(
    Output('main-graph', 'figure'),
    [Input('olympiad-type-dropdown', 'value'),
     Input('year-dropdown', 'value'),
     Input('grade-dropdown', 'value')]
)
def update_graph(olympiad_type, year, grade):
    point_data = load_point_data(olympiad_type, year, grade)

    return build_point_fig(
        point_data=point_data,
        forecast=get_forecast(point_data),
        point=get_point_by_year(olympiad_type, year, grade),
        title=f"{olympiad_type} {year} ({grade} класс)"
    )


@callback(
    Output('point-history-graph', 'figure'),
    [Input('olympiad-type-dropdown', 'value'),
     Input('grade-dropdown', 'value')]
)
def update_history_graph(olympiad_type, grade):
    return build_point_history_fig(
        point_history=load_point_history_data(olympiad_type, grade),
        title=f"{olympiad_type} ({grade} класс)"
    )
