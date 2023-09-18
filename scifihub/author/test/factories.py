import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "author.User"
    
    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    full_name = factory.Faker('name')
