import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# تحميل البيانات
df = pd.read_csv(
    "D:/DEPI/AMIT_DEPI_BNS5_AIS2_S1/src/Data Analysis/Dash/Dash.csv"
)

# إنشاء التطبيق
app = Dash(__name__)

app.title = "Interactive Dashboard"

# الأعمدة الرقمية
num_cols = df.select_dtypes(include="number").columns

# Layout
app.layout = html.Div([
    
    html.H1("Interactive Dashboard with Pie Plot"),
    
    html.Label("Choose your filter"),
    
    dcc.Dropdown(
        id="column-dropdown",
        options=[
            {"label": col, "value": col}
            for col in num_cols
        ],
        value=num_cols[0]
    ),
    
    dcc.Graph(id="pie-chart")
])


# Callback
@app.callback(
    Output("pie-chart", "figure"),
    Input("column-dropdown", "value")
)
def updatePie(select_col):

    grouped = (
        df.groupby("Area")[select_col]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        grouped,
        names="Area",
        values=select_col,
        title=f"Distribution of {select_col} by Area",
        hole=0.6,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    return fig


# تشغيل التطبيق
if __name__ == "__main__":
    app.run(
        debug=True,
        port=8051
    )