FROM python:3.11
WORKDIR /code
COPY . /code
ENV PYTHONUNBUFFERED=1
RUN pip3 install -r requirements.txt
EXPOSE 6000
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT [ "./gunicorn_starter.sh"]