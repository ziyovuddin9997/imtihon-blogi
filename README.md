# Blog API System

Django REST Framework yordamida yaratilgan Blog API tizimi.

## Features

- User Registration
- User Login / Logout
- Profile Management
- CRUD Posts
- CRUD Comments
- Like / Unlike Posts
- Token Authentication
- Search
- Filter
- Ordering

## Technologies

- Python 3.11+
- Django
- Django REST Framework
- Django Filter
- Pillow
- Python Decouple

## Installation

```bash
git clone <repository_url>
cd project_folder
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

`.env`

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Authentication

### Register

```http
POST /register/
```

### Login

```http
POST /login/
```

### Logout

```http
POST /logout/
```

## Endpoints

### Users

| Method | Endpoint |
|----------|------------|
| POST | /register/ |
| POST | /login/ |
| POST | /logout/ |
| GET | /profile/ |
| PUT | /profile/ |

### Posts

| Method | Endpoint |
|----------|------------|
| GET | /posts/ |
| POST | /posts/ |
| GET | /posts/{id}/ |
| PUT | /posts/{id}/ |
| DELETE | /posts/{id}/ |

### Comments

| Method | Endpoint |
|----------|------------|
| GET | /comments/ |
| POST | /comments/ |
| GET | /comments/{id}/ |
| PUT | /comments/{id}/ |
| DELETE | /comments/{id}/ |

### Likes

| Method | Endpoint |
|----------|------------|
| POST | /like/ |
| DELETE | /unlike/ |

## Search

```http
GET /posts/?search=django
```

## Filter

```http
GET /posts/?category=1
```

## Ordering

```http
GET /posts/?ordering=created_at
```

```http
GET /posts/?ordering=-created_at
```

## Author

Ziyovuddin
