from dash import Dash, html, dcc



app = Dash(__name__)



markdown_text = """ ## Dash Mardown

This is an example of a markdown in Dash   
Here is how you can add a link  with this syntax [CommonMark](http://commonmark.org/),  simple way right?  
Checkout here for more information about the syntax in this markdown [60 second tutorial for Dash](http://commonmark.org/help/) I guess this is enough for you guys.


To test this markdown syntax, I added this link for my [Github repository](https://github.com/Bamamou) for **Nicolas Bammaou**. This is the image on my github repository ![Profile photo][1] 
[1]:https://avatars.githubusercontent.com/u/99571735?v=4 "Nicolas Bamamou"  

 How does it look?  
 Below is how we can add code:   
 let's asssume that `x=1` that means `x+3=4`

 A loop in JavaScript:

    var i;
    for (i=0; i<5; i++) {
      console.log(i);
    }"""

app.layout = html.Div([dcc.Markdown(children= markdown_text)])

if __name__ == '__main__':
    app.run(debug = True)