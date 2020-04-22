import dash
import dash_core_components as dcc
import dash_html_components as html
import redis

from dash.dependencies import Output, Input
from flask import Flask

# Create app.
server = Flask(__name__)
app = dash.Dash(server=server)
app.layout = html.Div([dcc.Graph(id="result"), dcc.Interval(id="poller", interval=1000)])


# Create callbacks.
@app.callback(Output("result", "figure"), [Input("poller", "n_intervals")])
def poll_result(n_intervals):
    # Connect to redis.
    r = redis.Redis(host='myapp-redis', port=6379, db=0)
    # Get sensor value.
    sensor_value = r.get("mysensor").decode("utf-8")
    # Create graph.
    return dict(data=[dict(x=[0], y=[int(sensor_value)], type="bar")],
                layout=dict(yaxis=dict(range=[0, 10]), title="Sensor value"))


if __name__ == '__main__':
    app.run_server()
