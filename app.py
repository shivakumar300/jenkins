import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data for the dashboard
np.random.seed(42)
df = pd.DataFrame({
    'Date': pd.date_range(start='2025-01-01', periods=30, freq='D'),
    'Value': np.random.randn(30).cumsum(),
    'Category': np.random.choice(['A', 'B', 'C'], 30)
})

# Define the dashboard layout
app.layout = html.Div([
    html.H1('Simple Dash Dashboard', style={'textAlign': 'center', 'margin': '20px'}),
    
    # Dropdown for selecting category
    html.Div([
        html.Label('Select Category:'),
        dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
            value='A',
            style={'width': '50%', 'margin': '10px auto'}
        ),
    ], style={'textAlign': 'center'}),
    
    # Graph component
    dcc.Graph(id='line-graph'),
    
    # Data table
    html.Div([
        html.H3('Data Table'),
        dash.dash_table.DataTable(
            id='table',
            columns=[{'name': col, 'id': col} for col in df.columns],
            style_table={'overflowX': 'auto', 'margin': '20px'},
            style_cell={'textAlign': 'left', 'padding': '5px'},
        )
    ])
])

# Callback to update graph and table based on dropdown selection
@app.callback(
    [Output('line-graph', 'figure'),
     Output('table', 'data')],
    [Input('category-dropdown', 'value')]
)
def update_dashboard(selected_category):
    # Filter data based on selected category
    filtered_df = df[df['Category'] == selected_category]
    
    # Create line graph
    fig = px.line(
        filtered_df,
        x='Date',
        y='Value',
        title=f'Value Trend for Category {selected_category}',
        template='plotly_white'
    )
    
    # Prepare table data
    table_data = filtered_df.to_dict('records')
    
    return fig, table_data

# Run the app on port 8000 with host 0.0.0.0
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
