Blog API System
Loyiha haqida
Django Rest Framework yordamida yaratilgan Blog API tizimi. Foydalanuvchilar ro'yxatdan o'tishi, login qilishi, post yaratishi, comment yozishi va like bosishi mumkin.
O'rnatish
pip install -r requirements.txt python manage.py migrate python manage.py runserver 
Virtual Environment
python -m venv venv venv\Scripts\activate 
requirements.txt
Django
djangorestframework
djangorestframework-authtoken
django-filter
python-decouple
Pillow
.env namunasi
SECRET_KEY=9997 DEBUG=True ALLOWED_HOSTS=127.0.0.1,localhost 
API Endpoints
Authentication
POST /register/
POST /login/
POST /logout/
GET /profile/
PUT /profile/
Posts
GET /posts/
POST /posts/
GET /posts//
PUT /posts//
DELETE /posts//
Comments
GET /comments/
POST /comments/
PUT /comments//
DELETE /comments//
Likes
POST /like/
DELETE /unlike/
Qo'shimcha
Token Authentication
Search
Filter
Ordering
Image Upload
Owner Permissions