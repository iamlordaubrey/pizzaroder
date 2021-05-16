### PizzaRoder
A pizza ordering service implemented using the Django Rest Framework

&nbsp;

##### Endpoints
Making use of ViewSets handles our endpoints for us

| HTTP verbs    | Customer URL      | Order URL     |
| ---           | ---               | ---           |
| GET           | /customers        | /orders       |
|               | /customers/\<id>  | /orders/\<id> |

&nbsp;

##### Run
###### Local
To run locally, follow the steps:
- `create a postgres database`
- `git clone git@github.com:iamlordaubrey/pizzaroder.git`
- `cd pizzaroder`
- `python3 -m venv <environment name>`
- `source <environment name>/bin/activate`
- `pip install -r requirements.txt`

Create a `.env` file with the following database credentials:
```.dotenv
DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"
SQL_DBNAME=<database_name>
SQL_DBUSER=<database_user>
SQL_DBPASSWORD=<database_password>
```

afterwards run the following:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

&nbsp;

###### Docker
To run via Docker, ensure docker is installed and running, then follow the steps:
- `docker compose up -d --build`
- `docker compose up`

Stop and remove containers:
- `docker compose down -v`

The app can be accessed using the browsable api at `localhost:8000`

&nbsp;

##### Filter
To filter by status or customer, using `status=delivered` and `customer=Johnny`

Status => http://localhost:8000/orders/?search=delivered

Customer => http://localhost:8000/orders/?search=Johnny

Alternatively, you can filter using the `Filters` button
