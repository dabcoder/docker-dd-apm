# docker-dd-apm
Sample app to use `analyzed_spans`

With Docker on MacOS:

- Build the flask app image with: `docker build -t flaskapp:1.0 .`
- Run it with `docker run -d -p 5000:5000 flaskapp:1.0`
- Download the Datadog agent image and run the agent container with:
```
docker run -d -p 127.0.0.1:8126:8126/tcp --name datadog-agent \
              -v /var/run/docker.sock:/var/run/docker.sock:ro \
              -v /proc/:/host/proc/:ro \
              -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
              -e DD_API_KEY=<your_api_key> \
              -e DD_APM_ENABLED=true \
              -e DD_APM_NON_LOCAL_TRAFFIC=true \
              -e DD_APM_ANALYZED_SPANS="flask|flask.request=1,flask|flask.dispatch_request=1" \
              datadog/agent:latest
```
- Run `curl 0.0.0.0:5000` a few times
- Check the APM page on Datadog - trace search