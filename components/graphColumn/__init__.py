from dash import html

from .plotComponent import PlotComponent


GraphColumn = html.Div(
    className="graph-column",
    children=[
        PlotComponent
    ]
)

__all__ = ('GraphColumn', )

# def GraphColumn():
#     return html.Div(
#         id='graph-container',
#         className="graph-column",
#         children=[
#             PlotComponent,
#
#         ]
#     )
