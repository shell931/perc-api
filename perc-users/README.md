# PERC USERS SVC

Service to __SERVICE_SUMMARY__.

## SETUP

### SETUP YOUR VENV

```bash
# linux
python -m venv .venv
source .venv/bin/activate
```

### INSTALL REQUIREMENTS ON YOUR VENV

```bash
pip install --ignore-installed --no-cache-dir -r requirements.txt
```

## RESOURCES

ENDPOINT | METH
--|--
`/CreateUser/` | `PROTO GRPC`
`/GetAllUser/` | `PROTO GRPC`
`/SearchUsers/` | `PROTO GRPC`


### SETUP DOCKERFILE
```bash
FROM python:3.11
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
EXPOSE 50057
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT [ "./gunicorn_starter.sh"]
```

### SETUP DOCKER-COMPOSE
```bash
version: '3.7'
services:
  my-awesome-api:
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    container_name: perc-users
    ports:
      - 50057:50057
    environment:
      MI_ENV_VARIABLE: "example"
```

### SETUP GUNICORN
```bash
#!/bin/sh
gunicorn --workers 2 --threads 2 -b 0.0.0.0:50057 main:app
```

### DEPLOY DOCKER CONTAINER
```bash
# to build
docker-compose up --build
# To run with daemon up
docker-compose up -d
```

### GENERATE PROTOBUFS
```bash
python -m grpc_tools.protoc -I app/protobufs --python_out=. --grpc_python_out=. app/protobufs/recommendations.proto
```

# ACKNOWLEDGMENTS

Thanks to all Perc team.

---

* Powered by [Carlos Arriero](mailto:carlos.arriero931@gmail.com) 😎

