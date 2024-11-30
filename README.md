# PERC API

Servicios de administración de usuarios, creación de usuarios, listar todos los usuarios y filtrar por parametros.

## DOCUMENTACIÓN DE APIS
La documentación de la api se encuentra en los archivos:
* ### CreateUser
**swagger_create_user.yaml** -> Creación de usuarios
```bash
URL: 44.196.225.20:6000/api/v1
PATH: /PercServices/CreateUser
TYPE: POST
PAYLOAD EXAMPLE:
{
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  } 
REQUEST EXAMPLE:
{
    "data": {
        "email": "Sincere@april.biz",
        "httpCode": 201,
        "messaje": "User created success",
        "name": "Leanne Graham",
        "username": "Bret"
    },
    "status": 201
}
```
* ### GetAllUser
**swagger_get_all_users.yaml** -> Lista todos los usuarios
```bash
URL: 44.196.225.20:6000/api/v1
PATH: /PercServices/GetAllUser
TYPE: GET
REQUEST EXAMPLE:
{
    "totalUsers": 10,
    "users": [
        {
            "city": "Gwenborough",
            "company": "Romaguera-Crona",
            "name": "Leanne Graham"
        },
        {
            "city": "Wisokyburgh",
            "company": "Deckow-Crist",
            "name": "Ervin Howell"
        },
        .........
    ]
}
```
* ### SearchUsers
**swagger_filter_users.yaml** -> filtrado de usuarios por los parametros (name, city, company_name, order_by)  
Tenga en cuenta que el parametro de ordenamiento order_by se basa en los campos de busqueda (name, city, company_name) del mismo request
```bash
URL: 44.196.225.20:6000/api/v1
PATH: /PercServices/SearchUsers
TYPE: POST
PAYLOAD EXAMPLE:
{
    "name": "Le",
    "city": "",
    "company_name": "",
    "order_by": "city"
}
REQUEST EXAMPLE:
{
    "totalUsers": 5,
    "users": [
        {
            "city": "Bartholomebury",
            "company": "Yost and Sons",
            "name": "Glenna Reichert"
        },
        {
            "city": "Gwenborough",
            "company": "Romaguera-Crona",
            "name": "Leanne Graham"
        },
        ........
    ]
}
```

## ARQUITECTURA
El api esta desarrollado en python utilizando flask como framework y extendiendo una comunicación mediante microservicios implementando la tecnología de protobuf por protocolo grpc.  

Se ha desplegado en la nube de AWS mediante contenedores de docker los cuales son ejecutados por el archivo docker-compose.yml principal del proyecto.  

![Diagram](https://img-app-v1.s3.us-east-1.amazonaws.com/arc_perc_2.png "Diagram")  

Las ventajas de esta arquitectura es que se puede escalar y llevar a cualquier tipo de tecnologia como kubernetes, Eks, Vultr, Digital Ocean etc.  

Al utilizar proto se crea una comunicación mediante GRPC entre los servicios, esta tecnología trabaja bajo el lenguaje de C++ estableciendo una comunicación a bajo nivel y mas rapida.  

La comunicación del servicio principal si funciona mediante http para que cualquier usuario pueda consumir normalmente el api.  

Esta tecnología permite la comunicación con servicios desarrollados en otros lenguajes como java y go, lo que permite una mayor interoperabilidad

## SETUP

### SETUP DEPLOY ENTORNO LINUX

#### CREAR ENV'S  
```bash
 touch /home/perc-api/perc-api/.env
 touch /home/perc-api/perc-users/.env
```
#### CREAR VARIABLES DE ENTORNO perc-users/.env  
```bash
  vim perc-users/.env
  USER_API_URL=https://jsonplaceholder.typicode.com/users
```
#### EJECUTAR docker-compose.yml   
```bash
# linux
docker-compose up --build
```

### SETUP perc-api independiente para pruebas locales
[link](https://github.com/shell931/perc-api/tree/main/perc-api#readme)  

### SETUP perc-users independiente para pruebas locales
[link](https://github.com/shell931/perc-api/tree/main/perc-users#readme)  

# PRUEBAS
Para realizar los test unitarios se implemento pytest unicamente para el servicio de perc-users  
para ejecutar unicamente lanzar el comando "pytest" en la raiz del proyecto  
/Volumes/Portable/APPS/LOCAL/perc/perc-users/pytest

# MEJORAS  

* Se puede implementar un servicio de autenticación.
* Manejar un sistema de almacenamiento como mongo 
* Colocar dominio y certificado ssl mediante traefik 

# ACKNOWLEDGMENTS

Thanks to all PERC team.

---

* Powered by [Carlos Arriero](mailto:carlos.arriero931@gmail.com) 😎
