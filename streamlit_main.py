import  plotly.express as  px 
import  plotly.graph_objects as  go 
import numpy as  np 
import  scipy.stats as  ss
import  streamlit as  st
from sklearn.preprocessing import  StandardScaler 
from sklearn.linear_model import  LinearRegression 
from sklearn.linear_model import  LogisticRegression 
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import  KNeighborsRegressor
from sklearn.model_selection import  train_test_split
from dash import html, Dash, Input, Output, dcc, callback, dash_table
app = Dash(__name__)
models = {
    "Regression": LinearRegression, 
    "Decision Tree": DecisionTreeRegressor, 
    "KNN": KNeighborsRegressor
}
data = px.data.tips()
app.layout = html.Div([
    html.H1(children="Data with multiple  modelling  approaches"), 
    dash_table.DataTable(data=data.to_dict("record"), page_size=10),
    html.P("Select model:"), 
    dcc.Dropdown(
    id="dropdown", 
    options=[i for  i in models],  
    value= "Decision Tree"
    ), 
    dcc.Graph(figure={}, id="graph")
])
#creating  app callbacks
df = px.data.tips()
x = df.total_bill.values[:,None]
x_train, x_test, y_train, y_test = train_test_split(x, df.tip, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
x_range = np.linspace(x.min(), x.max(), 100)
y_range = model.predict(x_range.reshape(-1,1))
fig  = go.Figure([
  go.Scatter(x = x_train.squeeze(), y=y_train, name="Train", mode="markers"),
  go.Scatter(x= x_test.squeeze(), y=y_train, name="Test", mode="markers"),
  go.Scatter(x=x_range, y=y_range, name="predicted")
])
st.plotly_chart(fig, use_container_width=True)
