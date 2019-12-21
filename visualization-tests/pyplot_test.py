import plotly.express as expr

df = expr.data.iris()
fig = expr.scatter(
    df,
    x="sepal_width", y="sepal_length",
    color="sepal_length",
    color_continuous_scale='Magma',
)

fig.show()

import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))

fig.show()

import plotly.express as px

df = px.data.gapminder()
px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90])
