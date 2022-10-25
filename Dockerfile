FROM python:3
ARG ES_URL

ADD . /

RUN pip install -r requirements.txt
RUN sed -i "s/ES_URL/${ES_URL}/g" /config/config.ini

CMD [ "python3", "/flask_app.py" ]