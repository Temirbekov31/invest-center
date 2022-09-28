import os
from pathlib import Path
from pickle import TRUE

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-(*c05+7#3$=nt1d%euriog+#xzg-_2oo^hv^cumcshw6b-7mop'


DEBUG = True

ALLOWED_HOSTS = ["*"]


DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'invest',
        'USER': 'b_userdb',
        'PASSWORD': '050208852',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'root')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')




    # location /static/ {
    #     root /home/dony31/invest-center;
    #     expires 30d;
    # }
