import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-(*c05+7#3$=nt1d%euriog+#xzg-_2oo^hv^cumcshw6b-7mop'


DEBUG = True

ALLOWED_HOSTS = ["*"]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]