### Installing

After clone go to project folder:

```
cd social_network
```

Create virtual environment:
```
virtualenv -p python3.5 .venv
```

Activate virtualenv:
```
source .venv/bin/activate
```


Install requirements:
```
pip install -r requirements.txt
```
Create .env file:
```
touch .env
```
Add CLEARBIT_API_KEY, HUNTER_API_KEY and SENDGRID_API_KEY:
```
echo "CLEARBIT_API_KEY='your_api_key'" >> .env
echo "HUNTER_API_KEY='your_api_key'" >> .env
echo "SENDGRID_API_KEY='your_api_key'" >> .env
```

Use migrations:
```
python manage.py migrate
```

Create superuser:
```
python manage.py createsuperuser
```

Run server:
```
python manage.py runserver