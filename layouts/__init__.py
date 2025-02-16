from dash import html

from components import TextColumn, GraphColumn, HeaderComponent

BodyContainer = html.Div(
    className="body-container",
    children=[
        TextColumn,
        GraphColumn
    ]
)

Layout = html.Div(
    className="dashboard-container",
    children=[
        HeaderComponent,
        BodyContainer
    ]
)

__all__ = ('Layout', )
