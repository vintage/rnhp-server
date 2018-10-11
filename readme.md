# RNHP server

## Local development

```bash
$ virtualenv .venv -p python3
$ source .env/bin/activate
$ cd rnhp/
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py createsuperuser --username admin --email admin@example.com
$ ./manage.py runserver
```
