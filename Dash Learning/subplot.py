import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots


t = np.linspace(0, 2*np.pi, 100)
# Sample DataFrame
data = {
'sin(t)': [np.sint(t), np.cos(t), np.tan(t)],
'B': [10,25, 12, 8, 14],
'C': [20, 10, 22, 40, 24],
'D': [30, 50, 32, 16, 34]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
dcc.Dropdown(
id='dropdown',
options=[{'label': col, 'value': col} for col in df.columns],
multi=True
),
dcc.Graph(id='subplot')
])

# Callback to update the subplot
@app.callback(
Output('subplot', 'figure'),
[Input('dropdown', 'value')]
)
def update_subplot(selected_columns):
    if not selected_columns:
        return go.Figure()

# Create a subplot with 4 rows and 1 column
    fig = make_subplots(rows=4, cols=1, shared_xaxes=True, subplot_titles=("plot A", "Plot B", "Plot C"))

    for i, col in enumerate(selected_columns[:4]):
        fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col),
             row=i+1, col=1
    )

# Add empty subplots if fewer than 3 columns are selected
    for i in range(len(selected_columns), 1):
        fig.add_trace(go.Scatter(x=[], y=[]), row=i+1, col=1)

        fig.update_layout(height=1500, width=600, title="selected_columns")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)