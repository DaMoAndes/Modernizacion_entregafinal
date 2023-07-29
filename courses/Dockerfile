FROM python:3.9
WORKDIR /courses
ENV FLASK_APP=src/CoursesApp.py
ENV FLASK_DEBUG=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y netcat-traditional
RUN pip install --upgrade pip
COPY . /courses
RUN pip install -r requirements.txt
ENTRYPOINT ["sh","/courses/src/entrypoint.sh"]