import pandas as pd
import plotly.express as px

with open("JIRA_TITLE", "r") as f:
    TITLE = f.read()

df = pd.read_csv("plot.csv")
fig = px.bar(
    x=df["date"].tolist(),
    y=df["value"].tolist(),
    title=TITLE,
    labels={"y": "# Completed Issues", "x": ""},
)
fig.update_layout(margin=dict(l=80, r=80, t=100, b=80))
fig.write_html("plot.html", full_html=False, div_id="jira")
