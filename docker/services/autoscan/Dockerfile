FROM python:3.9-slim
WORKDIR /app
ADD ./services/autoscan /app/services/autoscan
RUN pip3 install --upgrade pip
RUN pip3 install -r services/autoscan/requirements.txt
ENV PYTHONUNBUFFERED="true"
ENTRYPOINT [ "python3", "-u", "services/autoscan/scan.py" ]