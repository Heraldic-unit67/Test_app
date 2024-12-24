import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

# Custom CSS styles
CARD_STYLE = {
    "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "borderRadius": "10px",
    "padding": "2rem",
    "backgroundColor": "rgba(255, 255, 255, 0.1)",
    "marginTop": "2rem",
}

app.layout = dbc.Container(
    [
        html.H1(
            "Fluid Quality Checker",
            className="text-center mb-4",
            style={"color": "#00bc8c", "fontWeight": "bold"},
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Label("Density", className="h5"),
                                    dbc.Input(
                                        id="density",
                                        type="number",
                                        placeholder="Enter Density...",
                                        className="mb-3",
                                    ),
                                ],
                                width=4,
                            ),
                            dbc.Col(
                                [
                                    dbc.Label("Temperature", className="h5"),
                                    dbc.Input(
                                        id="temperature",
                                        type="number",
                                        placeholder="Enter Temperature...",
                                        className="mb-3",
                                    ),
                                ],
                                width=4,
                            ),
                            dbc.Col(
                                [
                                    dbc.Label("Fluid Value", className="h5"),
                                    dbc.Input(
                                        id="fluid_value",
                                        type="number",
                                        placeholder="Enter Fluid Value...",
                                        className="mb-3",
                                    ),
                                ],
                                width=4,
                            ),
                        ],
                        className="g-4",
                    ),
                    dbc.Button(
                        "Compute Results",
                        id="compute-btn",
                        color="success",
                        size="lg",
                        className="w-100 mt-3",
                    ),
                    html.Div(
                        id="output",
                        className="mt-4 text-center h4",
                    ),
                ]
            ),
            style=CARD_STYLE,
        ),
    ],
    className="d-flex flex-column justify-content-start align-items-center py-4",
    style={"minHeight": "100vh", "backgroundColor": "#303030"},
    fluid=True,
)


@app.callback(
    Output("output", "children"),
    [
        Input("compute-btn", "n_clicks"),
        Input("density", "value"),
        Input("temperature", "value"),
        Input("fluid_value", "value"),
    ],
)
def update_result(n_clicks, density, temperature, fluid_value):
    if not n_clicks or density is None or temperature is None or fluid_value is None:
        return ""
    cons_temp = 15.0
    temp_stp = temperature - cons_temp
    calcu_temp = temp_stp * fluid_value
    total_value = density + calcu_temp

    if total_value >= 900:
        result = html.Span("BAD FUEL", style={"color": "#E74C3C"})
    elif total_value >= 800:
        result = html.Span("GOOD FUEL - READY FOR OFFLOAD", style={"color": "#00bc8c"})
    elif total_value >= 700:
        result = html.Span("GOOD FUEL - READY FOR OFFLOAD", style={"color": "#00bc8c"})
    else:
        result = html.Span("BAD FUEL", style={"color": "#E74C3C"})

    return [html.Div(f"Total Value: {total_value:.2f}", className="mb-2"), result]


if __name__ == "__main__":
    app.run_server(debug=True)
