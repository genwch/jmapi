FROM docker.io/library/python:3.7-slim-buster

ENV WORKDIR /usr/src/app
ENV PY_HOST 0.0.0.0
ENV PY_PORT 5000
ENV FLASK_APP jmapi

WORKDIR $WORKDIR
EXPOSE $PY_PORT

COPY ./requirements.txt $WORKDIR
RUN pip install -r requirements.txt
ADD ./$FLASK_APP $WORKDIR/$FLASK_APP
RUN /bin/echo -e "#!/bin/bash\nuvicorn $FLASK_APP:app --host=$PY_HOST --port=$PY_PORT" > /exec
RUN chmod a+x /exec

USER 1000

CMD ["/exec"]


