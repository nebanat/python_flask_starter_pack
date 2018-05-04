FROM python:3.5-slim
MAINTAINER Aaron Biliyok  <abiliyok@gmail.com>

ENV INSTALL_PATH /your_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "your_app.app:create_app()"
