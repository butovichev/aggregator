# import pytest

# from .models import GamerProfile
# from django.contrib.auth.models import User


# @pytest.fixture(scope='session')
# def user_data(f):
#     password = f.password()
#     return {
#         'username': f.user_name(),
#         'firstname': f.first_name(),
#         'lastname': f.last_name(),
#         'phone': f.phone_number(),
#         'email': f.email(),
#         'pass1': password,
#         'pass2': password,
#     }


# def test_signup_view(client):
#     response = client.get('/accounts/signup/')
#     assert response.status_code == 200


# @pytest.mark.django_db()
# def test_signup(client, f, user_data):
#     response = client.post('/accounts/signup/', user_data)
#     # assert response.status_code == 200

#     user = User.objects.get(username=user_data['username'])
#     assert user.username == user_data['username']

#     gamer = GamerProfile.objects.get(user=user)
#     assert user.id == gamer.user.id
#     assert gamer.phone == user_data['phone']

