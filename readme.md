# RNHP server

## Setup

```bash
$ virtualenv .venv -p python3
$ source .env/bin/activate
$ cd rnhp/
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py createsuperuser --username admin --email admin@example.com
$ ./manage.py runserver
```

## API

1. List messages - GET [http://localhost:8000/api/v1/messages/](http://localhost:8000/api/v1/messages/)
2. Create message - POST [http://localhost:8000/api/v1/messages/](http://localhost:8000/api/v1/messages/)
3. Like message - POST [http://localhost:8000/api/v1/messages/1/likes/](http://localhost:8000/api/v1/messages/1/likes/)
4. Start typing - POST [http://localhost:8000/api/v1/message-typings/](http://localhost:8000/api/v1/message-typings/)
5. Stop typing - DELETE [http://localhost:8000/api/v1/message-typings/mickiewicz/](http://localhost:8000/api/v1/message-typings/mickiewicz/)

## Dashboard

Admin available at [http://localhost:8000/admin/](http://localhost:8000/admin/)

- Username: admin
- Password: *the one set during setup phase*
