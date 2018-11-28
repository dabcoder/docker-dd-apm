from flask import Flask
from ddtrace import tracer
import os

# Add and initialize Datadog monitoring.
from datadog import initialize, statsd
initialize(statsd_host=os.environ.get('DATADOG_HOST'))

tracer.configure(
    hostname='datadog-agent',
    port=8126,
)

app = Flask(__name__)

@app.route('/')
def hello():
    # Increment a Datadog counter.
    statsd.increment('docker_compose_example.page.views')

    return 'Hello World!'

@app.route('/other')
def other_route():

    return 'Other route'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
