import dash
from dash import html
from dash import dcc
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the CSS styles
styles = {
    'body':{
        'background-color': 'black'
    },
    
    'container': {
        'max-width': '800px',
  
      
    },
    'title': {
        'text-align': 'center',
        'margin-bottom': '20px',
        'width': '1500px'
    },
    'chart-container': {
        'display': 'grid',
        'grid-template-columns': 'repeat(2, 1fr)',
        'grid-gap': '20px',
    },
    'chart': {
        'border': '1px solid #ddd',
        'border-radius': '5px',
        'padding': '10px',
        'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
    }
}

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1("ECG Data Visualization", style=styles['title']),
        dcc.Graph(id='ecg-bar-chart', style={ 'width': '100%'}),
        html.Div(
            style=styles['chart-container'],
            children=[
                dcc.Graph(id='ecg-pie-chart', style=styles['chart']),
                dcc.Graph(id='ecg-agepie-chart', style=styles['chart'])
            ]
        ),
        dcc.Graph(id='ecg-agebar-chart'),
        dcc.Graph(id='ecg-line-chart'),
    ],
    style=styles['container']
)

# Register the callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
