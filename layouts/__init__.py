from dash import html

from components import TextColumn, GraphColumn


Layout = html.Div(
    className="dashboard-container",
    children=[
        TextColumn,
        GraphColumn()
    ]
)

__all__ = ('Layout', )
