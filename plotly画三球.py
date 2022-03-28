import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

trace=go.Scatter(
    x=[1,2,3],
    y=[1,2,3],
    marker=dict(
        color=['red','blue','green'],
        size=[200,90,200]
    ),
     mode='markers+lines'
)
py.plot([trace])