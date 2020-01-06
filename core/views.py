# coding: utf-8
import json

from django.contrib import auth
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import activity_service, log_svc, todo_svc, user_service, globalsettings_svc


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        log_svc.log_login(request.user)
    return JsonResponse(user.to_dict_json(), safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': request.user.to_dict_json(),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


def register(request):
    user = json.loads(request.POST['user'])
    user = user_service.register(user)
    return JsonResponse(json.dumps(user.to_dict_json()), safe=False)


@ajax_login_required
def save_activity(request):  # TODO: checar se soh faz logado
    activity_json = json.loads(request.POST['activity'])
    activity = activity_service.add_activity(activity_json)
    activity_service.join_member(request.user, activity)
    return JsonResponse(json.dumps(activity.id), safe=False)


def get_activity(request):
    a = activity_service.get_by_id(request.GET['id'])
    return JsonResponse(json.dumps(a.to_dict_json()), safe=False)


def search_activity(request):
    platform = json.loads(request.GET.get('platform', "null"))
    name = json.loads(request.GET.get('name', "null"))
    date = json.loads(request.GET.get('date', "null"))
    data = []
    for activity in activity_service.search_activity(platform, name, date):
        data.append(activity.to_dict_json())
    return JsonResponse(json.dumps(data), safe=False)


def join_activity(request):
    id = json.loads(request.POST.get('activity_id', "null"))
    activity = activity_service.join_member(request.user, activity_service.get_by_id(id))
    return JsonResponse(json.dumps(activity.to_dict_json()), safe=False)


def leave_activity(request):
    id = json.loads(request.POST.get('activity_id', "null"))
    activity = activity_service.leave_member(request.user, activity_service.get_by_id(id))
    return JsonResponse(json.dumps(activity.to_dict_json()), safe=False)

def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)