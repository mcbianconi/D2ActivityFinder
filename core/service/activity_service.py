from core.models import Activity, User
import datetime
from django.db.models import Count
from django.core.exceptions import ValidationError

def add_activity(activity_dict):
    activity = Activity()
    activity.name = activity_dict["name"]
    activity.description = activity_dict["description"]
    activity.max_players = int(activity_dict["max_players"])
    activity.date = activity_dict["date"]
    activity.platform = int(activity_dict["platform"])
    activity.image = activity_dict["image"]
    activity.save()
    return activity

def join_member(member: User, activity: Activity):
    if activity.members.count() < activity.max_players:
        activity.members.add(member)
        activity.save()
        return activity
    else:
        raise ValidationError("Max members reached")

def leave_member(member: User, activity: Activity):
    activity.members.remove(member)
    activity.save()
    return activity

def get_by_id(id):
    return Activity.objects.get(pk=id)

def search_activity(platform, name, date):
    result = Activity.objects.annotate(num_players=Count('members'))
    result = result.filter(num_players__gt = 0)
    
    if date:
        dateobj = datetime.datetime.strptime(date, "%Y-%m-%d")
        result = result.filter(date__gte = dateobj)
    if name:
        result = result.filter(name__icontains=name)
    if platform and platform != -1:
        result = result.filter(platform=platform)
    
    return result

    
    
     