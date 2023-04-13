from dash import  Dash, html,dash_table, dcc 
from dash import  *
import plotly.express as px
import  pandas  as  pd
df = pd.read_csv("Documents/auto_mpg@wambugu.csv")
app = Dash(__name__)
app.layout = html.Div([
    html.Div(children="Data visualization app"),
    html.Hr(),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10, style_table={"overflowX": "auto"}),
    dcc.Graph(figure=px.scatter(df,x="Acceleration", y="MPG", animation_frame="Model Year", animation_group="Horsepower",size="Cylinders",hover_name="Origin", log_x=True,color="Origin")),
    dcc.RadioItems(options=["Displacement", "Acceleration", "Horsepower"], value = "MPG", id="conrols-and-radio-item"),
    dcc.Graph(figure={}, id="control-and-graph")
])
@callback(
    Output(component_id= "control-and-graph", component_property="figure"),
    Input(component_id = "conrols-and-radio-item", component_property="value")
)
def update_graph(col_choses):
    fig = px.scatter(df,y="MPG", x=col_choses, color="Origin")
    return fig

app.run_server(debug=True)