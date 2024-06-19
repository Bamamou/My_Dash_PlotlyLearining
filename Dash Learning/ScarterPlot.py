from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd



app = Dash(__name__)
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
fig =px.scatter(df, x="gdp per capita", y="life expectancy", size="population", color="continent", hover_name="country", log_x=True, size_max=60)

#Now let's set the layout colors of our app
fig.update_layout(
    plot_bgcolor ='#121212',    # The bg of the plot
    paper_bgcolor = '#121212',  # The bg of the paper 
    font_color = '#1876AE'      # The text on the plot (Inside the plot only)
)
# Now let's work on the layout itself
app.layout = html.Div(style= {'backgroundColor':'#121212', 'textAlign': 'center'}, children= [html.H1('Hello Dash'),
             html.Div(style= {'textAlign': 'center','backgroundColor': '#121212'}, children = 'This is simple scatar plot of the World life expectancy vs GDP'),

             dcc.Graph(id="life-exp-vsgdp", figure = fig)])


# let's run the app
if __name__ == '__main__':
    app.run(debug=True)