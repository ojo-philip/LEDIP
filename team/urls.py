from django.urls import path, include
from .views import (
    team_page,
)


app_name = 'team'
urlpatterns = [
    path('<int:pk>-<str:slug>/',
        team_page, name='team_page'),
]
