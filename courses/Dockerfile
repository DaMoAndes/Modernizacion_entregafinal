FROM python:3.9

WORKDIR /courses

ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional

COPY . /courses

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "run"]