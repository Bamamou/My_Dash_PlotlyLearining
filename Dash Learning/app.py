from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 



# create the app 
app = Dash(__name__)
df = pd.DataFrame({
    "Family": ["Apple", "Oranges", "Banana", " Apples", "oranges", "Banana", "peper", "Avocado"],
    "Amount": [ 4, 10, 25, 1, 5, 18, 25, 20],
    "City": ["CN", "AB", "DK", "ACC", "LG", "CT", "MV", "KY"]
})
fig = px.bar(df, x="Family", y="Amount", color="City", barmode="group" )
app.layout = html.Div(children=[html.H1('First Dash App'),
                                html.Div(children=""" A web application framework for my Data """),
                                
                                dcc.Graph(
                                    id='Example of a graph',
                                    figure= fig
                                )
                                
                                ])

if __name__ == '__main__':
    app.run(debug=True)