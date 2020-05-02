import os

MONGO_URI = os.getenv('MONGO_URI')

PAGINATION = False
HATEOAS = False
DEBUG = True

DOMAIN = {
    'objects': {
        'resource_methods': ['GET', 'POST']
        }
}
