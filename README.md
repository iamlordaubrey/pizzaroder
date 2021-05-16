### PizzaRoder
A pizza ordering service implemented using the Django Rest Framework


##### Endpoints
Making use of ViewSets handles our endpoints for us

| HTTP verbs    | Customer URL      | Order URL     |
| ---           | ---               | ---           |
| GET           | /customers        | /orders       |
|               | /customers/\<id>  | /orders/\<id> |
| POST          |


##### Run
To run locally, follow the steps:
- `git clone git@github.com:iamlordaubrey/pizzaroder.git`
- `cd pizzaroder`
- `python3 -m venv <environment name>`
- `source <environment name>/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

The app can be accessed using the browsable api at `localhost:8000`


##### Filter
To filter by status or customer, using status=delivered and customer=Johnny Depp

Status => http://localhost:8000/orders/?search=delivered

Customer => http://localhost:8000/orders/?search=Johnny

Alternatively, you can filter using the `Filters` button

search => 
    status => http://localhost:8000/orders/?search=delivered
    customer => http://localhost:8000/orders/?search=marco
    or using the `Filters` button besides the `OPTIONS` button (top right)
