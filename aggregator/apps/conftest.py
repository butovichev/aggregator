import pytest

from faker import Faker
from django.core.management import call_command


from django.contrib.auth.models import User
from aggregator.apps.geo.models import City



@pytest.fixture(scope='session')
def f():
    return Faker()


@pytest.fixture(scope='function')
@pytest.mark.django_db()
def user_staff(f):
    user = User()
    user.username = f.first_name(),
    user.email = f.email()
    user.password = f.password()
    user.is_staff = True
    user.save()
    return user


@pytest.mark.django_db()
@pytest.fixture(scope='function')
def user(f):
    return User.objects.create_user(username=f.first_name(),
                                    email=f.email(),
                                    password=f.password())


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'city.json')


def test_django_db_setup(django_db_setup):
    pass


@pytest.mark.django_db()
@pytest.fixture(scope='function')
def city_msk(f):
    return City.objects.filter(domain_name='msk')[:1].get()
