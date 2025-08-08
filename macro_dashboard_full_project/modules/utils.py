import dash_bootstrap_components as dbc
from dash import html

def create_card(title, data_dict):
    return dbc.Card([
        dbc.CardHeader(title, className="text-center fw-bold"),
        dbc.CardBody([
            html.Ul([
                html.Li(f"{key}: {value}") for key, value in data_dict.items()
            ], className="list-unstyled")
        ])
    ], className="m-1")
