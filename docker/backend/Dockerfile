FROM python:3.9-slim
WORKDIR /app
ADD ./backend/requirements.txt /app/backend/

RUN pip3 install --upgrade pip
RUN pip3 install gunicorn
RUN pip3 install -r backend/requirements.txt

ADD ./backend /app/backend
ADD ./docker /app/docker

# EXPOSE 8000