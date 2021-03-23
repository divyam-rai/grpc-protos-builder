FROM python:3.6
RUN mkdir -p /usr/src/app/logs
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt
VOLUME /usr/src/app/version.txt
CMD ["python", "main.py"]