from dash import dcc, html


def GraphColumn():
    return html.Div(
        id='graph-container',
        className="graph-column",
        children=[
            dcc.Graph(id='main-graph'),
            dcc.Store(id='data-store')
        ]
    )
