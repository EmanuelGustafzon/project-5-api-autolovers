# Autolovers API
Autolovers is the backend, the api for the webiste Autolovers Media. As you can hear it is a site for people who loves cars. It is a social media platform where users can review cars and share with the community. A user can create reviews, like and comment reviews, like comments, follow each other and even advertise cars for sale. This api is built with Django and django restframework.

## Press at this link https://autolovers.herokuapp.com/ to see the deployed api. by adding the app name in the end of the url you can access the json data for each app. For example https://autolovers.herokuapp.com/review

## The deployed frontend page you will find here: https://autoloversmedia.herokuapp.com/

## Agile methodology
Find the user stories and the project here: 

## Database
- The databse is structures as following
  - User is connected Profile, Review, Reviewlikes, comments, likes, commentlikes, market, follower.
  - Profile is connected to user.
  - Follower is connected to user. 
  - Review is connected to user, likes, comments.
  - Market is connected to user.
  - Commentlikes is connected to users and comments.
## PEP8
The code passed without errors in pep8.

## Manual testing
  - Tested all the urls.
  - Tested all the forms and crud functionality so the database is updating for  review, market, likes, commentlikes, profiles, comments and follower. I did this by entering each url and creating, updating and deleting data. I also did all this through the frontend page. 
  - Tested serializers so the modules get translated to json.
  - Tested that the filters is working for reviews and market.

## bugs
- there was a bug that users could not logout, this was fixed by creating a logout view. I forgot to add queryset to the profile detailview and review detail view so the likes_count, comments_count and following_count and folowed_count did not show up.

## none fixed bugs.
  - none so far. 

## none fixed bugs.
  - none 


## Technologies Used:
  - Python
  - django
  - Django rest framework
  - Cloudinary storage
  - Heroku
  - Pillow
  - Django Rest Auth
  - PostgreSQL
  - Cors Headers
  - 

## deployment

- Create GitHub repositry
- Use the template provided by Code Institute.
- Open GitPod workspace.
- Create Heroku app.
- Add the Postgres package to the Heroku app via the Resources tab.
- pip install following commands:
  - 'django<4'
  - dj3-cloudinary-storage
  - Pillow
  - djangorestframework
  - django-filter
  - dj-rest-auth
  - 'dj-rest-auth[with_social]'
  - djangorestframework-simplejwt
  - dj_database_url psycopg2
  - gunicorn
  - django-cors-headers
- create Django project with the command: django-admin startproject project_name .
- Add these config vars in heroku:
  - Key: SECRET_KEY | Value: hidden
  - Key: CLOUDINARY_URL | Value: cloudinary://hidden
  - Key: DISABLE_COLLECTSTATIC | Value: 1
  - Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com

- Connect to the frontend by adding these config vars in Heroku:
  - Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
  - Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io

- import to settings.py
import dj_database_url
import re
import os
if os.path.exists('env.py')
    import env

- Add cloudinery storage in setting.py:
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'

- below installed apps add: SITE_ID = 1
- Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
- Set JSON as default rendering:
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
- under Json default rendering add:
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

Then add:
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
- set debug to: DEBUG = 'DEV' in os.environ
- Update database varible:
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
- Add the Heroku app to the ALLOWED_HOSTS variable:
os.environ.get('ALLOWED_HOST'),
'localhost',
- Underneath add CORS_ALLOWED varible:
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
- Add 'corsheaders.middleware.CorsMiddleware', to MIDDLEWARE
- A tutor also wold me to add: CORS_ORIGIN_ALLOW_ALL = True
- Create a Procfile and add:
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
- Migrate all to the database:
python3 manage.py makemigrations
python3 manage.py migrate
- Freeze the requirements.txt
pip3 freeze --local > requirements.txt
- Push all to github by git add . , git commit and git push.
- Finally deploy in Heroku. 

## Credits
- Code Institute Docs.
- Tutors and slack.
- Stackoverflow
- Django docs.



