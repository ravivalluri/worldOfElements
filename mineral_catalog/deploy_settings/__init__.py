import dj_database_url

from mineral_catalog.settings import *

DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    '0.0.0.0'
]

SECRET_KEY = get_settings_var("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)