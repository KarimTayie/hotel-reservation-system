# Hotel reservation system
A backend system to handle hotel room reservations.

## Features

1. Room Management :
   * Add a new room with details: room number, type (e.g., single, double, suite), and price
   per night.
   * List all available rooms for a given date.
​
1. Reservation Management :
   * Make a reservation using a room number and specific dates.
   * Cancel a reservation.
​
1. User Management :
   * Register a new user (guest).
   * Authenticate a user using username and password.

## Apis
- users/create/ 

## 	Prerequisites

make sure to use python version 3.11

Install virtualenv

On macOS and Linux:
```json
$ python3 -m pip install --user virtualenv
```

On Windows:
```json
$ py -m pip install --user virtualenv
```


Create virtualenv

On macOS and Linux:
```json
$ python3 -m venv .venv
```

On Windows:
```json
$ py -m venv .venv
```


Activate virtualenv

```json
$ source .venv/bin/activate
```


Install all project dependencies

```json
$ pip install -r /requirements.txt
```

## How to run

### Default

You can run the application from the command line with manage.py. Go to the root folder of the application.

Run migrations:

```json
$ python manage.py migrate
```

Run server on port 8000:

```json
$ python manage.py runserver 8000
```

## API Doc

Postman API collection link:
[Postman collection](https://api.postman.com/collections/5401296-a6aa87be-6955-469b-ae4e-1ad67119e249?access_key=PMAT-01HBMGCJHY9FK343CWNBZSDTEE)