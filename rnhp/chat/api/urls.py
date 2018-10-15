from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = 'chat'

router = routers.SimpleRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'message-typings', views.MessageTypingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
