import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: fake.email())
    password = 'password'
    first_name = factory.Sequence(lambda n: fake.first_name())
    username = first_name
    is_superuser = True
    is_staff = True
    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.raw_password = password
            user.set_password(password)
            if create:
                user.save()
        return user
