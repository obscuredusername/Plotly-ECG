from dash.dependencies import Input, Output
import data_utils
import chart_utils

# Fetch the data and headers
data, headers = data_utils.fetch_selected_data()

# Define the callback function to update the pie chart
def update_pie_chart(chart_id):
    figure = chart_utils.generate_pie_chart(data, headers)
    return figure
def update_agepie_chart(chart_id):
    figure = chart_utils.generate_agepie_chart(data, headers)
    return figure

def update_bar_chart(chart_id):
    figure = chart_utils.generate_bar_chart(data, headers)
    return figure
def update_agebar_chart(chart_id):
    figure = chart_utils.generate_agebar_chart(data, headers)
    return figure
def update_line_chart(chart_id):
    figure = chart_utils.generate_line_chart(data, headers)
    return figure

# Register the callback functions
def register_callbacks(app):
    @app.callback(
        Output('ecg-pie-chart', 'figure'),
        [Input('ecg-pie-chart', 'id')]
    )
    def update_pie_chart_callback(chart_id):
        return update_pie_chart(chart_id)
    @app.callback(
        Output('ecg-agepie-chart', 'figure'),
        [Input('ecg-agepie-chart', 'id')]
    )
    def update_agepie_chart_callback(chart_id):
        return update_agepie_chart(chart_id)

    @app.callback(
        Output('ecg-bar-chart', 'figure'),
        [Input('ecg-bar-chart', 'id')]
    )
    def update_bar_chart_callback(chart_id):
        return update_bar_chart(chart_id)
    @app.callback(
        Output('ecg-agebar-chart', 'figure'),
        [Input('ecg-agebar-chart', 'id')]
    )
    def update_agebar_chart_callback(chart_id):
        return update_agebar_chart(chart_id)
    @app.callback(
        Output('ecg-line-chart', 'figure'),
        [Input('ecg-line-chart', 'id')]
    )
    def update_line_chart_callback(chart_id):
        return update_line_chart(chart_id)

# Assuming the Dash app instance is already created and assigned to the variable 'app'
