FROM python:3.11
RUN mkdir /app
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip3 install -r requirements.txt
EXPOSE 50057
ENTRYPOINT [ "python", "main.py" ]