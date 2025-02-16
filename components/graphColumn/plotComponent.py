from dash import dcc, html


PlotComponent = html.Div(
    id='graph-container',
    className="plot-column",
    children=[
        dcc.Graph(id='main-graph'),
        dcc.Graph(id='point-history-graph'),
        dcc.Store(id='data-store')
    ]
)
