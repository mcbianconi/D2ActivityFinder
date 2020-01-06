from core import views
from django.urls import path

urlpatterns = [
    path('api/settings', views.settings),
    path('api/dapau', views.dapau),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/whoami', views.whoami),
    path('api/register', views.register),
    path('api/activity', views.save_activity),
    path('api/get_activity', views.get_activity),
    path('api/search_activity', views.search_activity),
    path('api/activity/join', views.join_activity),
    path('api/activity/leave', views.leave_activity),  
]
