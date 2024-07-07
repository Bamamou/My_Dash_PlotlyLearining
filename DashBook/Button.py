# from dash import Dash, html

# #create an App 
# app = Dash(__name__)
# # Create a button 
# button = html.Button("Click Me")
# # Create the layout of the app and place the button
# app.layout = html.Div(button)

# # Run the app
# if __name__  == "__main__":
#     app.run(debug=True)


# # Dash Boostrap dbc.Button
# import dash
# from dash import Dash, html
# import dash_bootstrap_components as dbc
# # Create an app 
# app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY]) # CYBORG, BOOTSTRAP, SOLAR, MINTY
# button1 = html.Div( children=
#     [
#         dbc.Button("Primary", color = "primary", className ="me-2"),
#         dbc.Button("Secondary", color = "secondary", className ="me-2"),
#         dbc.Button("Warning", color = "warning", className ="me-2", active =True),
#         dbc.Button("Success", color = "success", className ="me-2", disabled=True),
#         dbc.Button("Danger", color = "danger", className ="me-2",outline=True,),
#         dbc.Button("Information", color = "info", className ="me-2", download ="link"),
#         dbc.Button("Link", color = "link", className ="me-2", external_link =True),
#     ], className = "m-4"
    
# )

# button2 = html.Div( children=
#     [
#         dbc.Button("Warning", color = "warning", className ="me-2", active =True),
#         dbc.Button("Secondary", color = "secondary", className ="me-2"),
#         dbc.Button("Success", color = "success", className ="me-2", size="lg"),
#         dbc.Button("Primary", color = "primary", className ="me-2", disabled=True),
#         dbc.Button("Information", color = "info", className ="me-2", download ="link"),
#         dbc.Button("Danger", color = "danger", className ="me-2"),
#         dbc.Button("Link", color = "link", className ="me-2"),
#     ], className = "m-3"
# )

# app.layout = (dbc.Container(button1), dbc.Container(button2))

# if __name__ == "__main__":
#     app.run_server(debug=True)


# Dash Boostrap dbc.Button
from dash import Dash, html
import dash_bootstrap_components as dbc
# Create an app 
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME, dbc.icons.BOOTSTRAP]) # CYBORG, BOOTSTRAP, SOLAR, MINTY

button1 = html.Div( children=
    [
        dbc.Button([html.I(className="fa-solid fa-cloud-arrow-down me-2"), "Download"], color = "primary", className ="me-2"),
        dbc.Button([html.I(className="bi bi-gear me-2"), "Settings"], color = "secondary", className ="me-2"),
        dbc.Button("Warning", color = "warning", className ="me-2", active =True),
        dbc.Button("Success", color = "success", className ="me-2", disabled=True),
        dbc.Button("Danger", color = "danger", className ="me-2",outline=True,),
        dbc.Button("Information", color = "info", className ="me-2", download ="link"),
        dbc.Button("Link", color = "link", className ="me-2", external_link =True),
    ], className = "m-4"
    
)
# the me-2 stands for marging of 2 dp
button2 = html.Div( children=
    [
        dbc.Button("Warning", color = "warning", className ="me-2", active =True),
        dbc.Button("Secondary", color = "secondary", className ="me-2"),
        dbc.Button("Success", color = "success", className ="me-2", size="lg"),
        dbc.Button("Primary", color = "primary", className ="me-2", disabled=True),
        dbc.Button([html.I(className="bi bi-cloud-drizzle-fill me-2"), "Heading"], color = "info", className ="me-2", download ="link"),
        dbc.Button([html.I(className="bi bi-bicycle me-2"), "Bicycle "], color = "danger", className ="me-2"),
        dbc.Button("Link", color = "link", className ="me-2"),
    ], className = "m-3"
)

app.layout = (dbc.Container(button1), dbc.Container(button2))

if __name__ == "__main__":
    app.run_server(debug=True)