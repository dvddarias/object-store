import os

MONGO_URI = os.getenv('MONGO_URI')

PAGINATION = False
HATEOAS = False
DEBUG = False

DOMAIN = {
    'objects': {
        'resource_methods': ['POST'],
        'allow_unknown': True
        }
}
