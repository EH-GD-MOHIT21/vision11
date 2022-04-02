from django.urls import path
from . import consumers
websocket_urlpatterns=[
    path('ws/sc/<str:groupname>/<str:pid>/',consumers.MyASyncConsumer.as_asgi()),
]