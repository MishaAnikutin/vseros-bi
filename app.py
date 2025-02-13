from dash import Dash

from callbacks import *
from layouts import Layout


app = Dash(__name__)
app.layout = Layout


if __name__ == "__main__":
    app.run_server(debug=True)
