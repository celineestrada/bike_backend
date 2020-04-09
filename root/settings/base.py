INSTALLED_APPS = (
    'dijango_admin_bootstrapped',
    'django.contrib.gis',
    'django_filters',
    'rest_framework',
    'api'
)

CLUSTER_ZOOM_LIMIT = 14
ANYCLUSTER_GEODJANGO_MODEL_ACCIDENT_POINT = 'api.accident_point'
ANYCLUSTER_COORDINATES_COLUMN = 'id'
GMAPS_BROWSER_TOKEN = 'GOOGLE_MAPS_TOKEN_GOES_HERE'

DATABSES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '8080'
    }
}

REDIS_OPTIONS = {
    'conn': {
        'host': 'localhost',
        'port': 5000,
        'timeout': 3,
        'password': None
    }
}
