from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=35)
    gamer_tag = models.CharField(max_length=35)
    avatar = models.CharField(max_length=100, default="/avatar_placeholder.png")

    def to_dict_json(self):
        d = {
            'id': self.id,
            'name': self.username,
            'username': self.username,
            'email': self.email,
            'gamer_tag': self.gamer_tag,
            'avatar': self.avatar
        }
        return d

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.SET_NULL)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }

class Activity(models.Model):
    platform = models.SmallIntegerField()
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=150)
    max_players = models.PositiveSmallIntegerField()
    date = models.DateField()
    members = models.ManyToManyField(User, related_name="activities")
    image = models.CharField(max_length=100, default="/activity_placeholder.jpg")

    def to_dict_json(self):
        d = {
            'id': self.id,
            'platform': self.platform,
            'name': self.name,
            'description': self.description,
            'max_players': self.max_players,
            'date': str(self.date),
            'image': self.image
        }
        d["members"] = []
        if self.members.exists():
            for member in self.members.all():
                d["members"].append(member.to_dict_json())
        return d

