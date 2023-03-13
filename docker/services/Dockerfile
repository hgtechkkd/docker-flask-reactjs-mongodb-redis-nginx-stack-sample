FROM python:3.9-slim
WORKDIR /app
ADD ./services/requirements.txt /app/services/

RUN pip3 install --upgrade pip
# RUN pip3 install gunicorn
RUN pip3 install python-dotenv
RUN pip3 install -r services/requirements.txt

# COPY ./services/aws-credentials /app/.aws/credentials
ADD ./services /app/services
# ADD ./docker /app/docker

# EXPOSE 8000
# RUN python services/s3/auto_scan_s3.py
ENTRYPOINT [ "python3", "services/s3/auto_scan_s3.py" ]