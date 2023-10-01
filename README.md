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

# Database
## Tables
1. Room:
   * id (Primary Key)
   * room_number (Unique Integer): Unique identifier for each room.
   * room_type (String): Type of the room (e.g., single, double, suite).
   * price_per_night (Decimal): Price per night for the room.

2. User (Django Default User Model):
   * id (Primary Key)
   * username (String): Unique username for authentication.
   * password (String): User password (hashed for security).
   * ... (Other fields from Django's default User model, such as email, first name, last name, etc.)

3. Reservation:
   * id (Primary Key)
   * start_date (Date): Start date of the reservation.
   * end_date (Date): End date of the reservation.
   * is_cancelled (Boolean): Indicates if the reservation is canceled or active.
   * room_id (Foreign Key): References the room_number field in the Room table.
   * user_id (Foreign Key): References the id field in the User table.

## Relationships:
* Reservation and Room:
  * Foreign Key: room_id in the Reservation table links to the room_number field in the Room table.
  * Relationship: Many reservations can be associated with one room.

* Reservation and User:
  * Foreign Key: user_id in the Reservation table links to the id field in the User table.
  * Relationship: Many reservations can be associated with one user (guest).

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

## Notes
- Only admin users can create rooms. you can create an admin by running this command:
```json
$ python manage.py createsuperuser
```
- You can only cancel room reservations that you have reserved by the same user.