FROM python:3.9-slim
WORKDIR /app
ADD ./services/s3 /app/services/s3
RUN pip3 install --upgrade pip
RUN pip3 install -r services/s3/requirements.txt
ENV PYTHONUNBUFFERED="true"
ENTRYPOINT [ "python3", "-u", "services/s3/scan_s3.py" ]