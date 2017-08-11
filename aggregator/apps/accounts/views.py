from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from .models import Gamer, Partner
from .forms import UserForm
from aggregator.apps.comments.models import Comment


def signup(request):
    user = User()
    user_form = UserForm(request.POST, instance=user)
    if request.method == "POST" and user_form.is_valid():
        data = user_form.cleaned_data
        if data['user_type'] == 'partner':
            _signup_partner(data, user)
        elif data['user_type'] == 'gamer':
            _signup_gamer(data, user)
        else:
            raise ValueError()

    return render(request, "signup.html", {
        "user_": user,
        'user_form': user_form,
    })


def _signup_gamer(data, user):
    gamer = Gamer()

    user.username = data['username']
    user.first_name = data['firstname']
    user.last_name = data['lastname']
    user.email = data['email']
    user.set_password(data['pass1'])

    user.save()

    group_gamer = _get_group_and_permission()
    user.groups.add(group_gamer)

    gamer.user = user

    gamer.save()


def _signup_partner(data, user):
    pass


def _get_group_and_permission():
    new_group, created = Group.objects.get_or_create(name='gamer')

    ct = ContentType.objects.get_for_model(Comment)
    permission, _ = Permission.objects.get_or_create(codename='can_add_comments',
                                                     name='Can add comments',
                                                     content_type=ct)
    new_group.permissions.add(permission)

    return new_group


@login_required
def my_profile(request):
    user = request.user
    return render_to_response("accounts/card.html", {"user": user},
                              context_instance=RequestContext(request))
