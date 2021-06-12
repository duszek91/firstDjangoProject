
## Fixtures

https://docs.djangoproject.com/en/3.2/howto/initial-data/

https://docs.djangoproject.com/en/3.2/ref/django-admin/#django-admin-dumpdata


from django.test import TestCase

class MyTestCase(TestCase):
    fixtures = ['/myapp/fixtures/dump.json',]
    ...

## Factory boy


https://factoryboy.readthedocs.io/en/stable/index.html