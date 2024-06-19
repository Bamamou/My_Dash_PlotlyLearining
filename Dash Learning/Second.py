from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#202020',
    'papercolor': '#202020',
    'text': '#7FDBFF'
}
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x= "Fruit", y="Amount", color= "City", barmode= 'group')
fig.update_layout(
    plot_bgcolor = colors['202020'],
    paper_bgcolor = colors['202020'],
    font_color = colors['#7FDBFF']
)
app.layout = html.Div( children=[ html.H1('Hello Dash', style={'textAlign': 'center', 'color': colors["text"]}, style= {'backgroundColor': colors["background"]}),
             html.Div(children='Dash: A web application framework for your data.', style={'textAlign': 'center',  'color': colors['text']}),
    dcc.Graph(
        id ='Second exaples',
        figure = fig
    )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)