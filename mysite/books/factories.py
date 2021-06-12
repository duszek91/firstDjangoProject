import factory

from .models import Book

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    author = "Ala Alińska" # factory.SubFactory(AuthorFactory)
    title = factory.Sequence(lambda n: 'Title %s' % n)
    description = factory.Sequence(lambda n: 'Description %s' % n)
