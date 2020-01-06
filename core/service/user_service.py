from core.models import User
from django.contrib import auth


def register(user):
    u = User()
    u.email = user['email']
    u.gamer_tag = user['gamer_tag']
    u.username = user['name']
    u.name = user['name']
    u.set_password(user['password'])
    u.avatar = user['avatar']
    u.save()
    return u