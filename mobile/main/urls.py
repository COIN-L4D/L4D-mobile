from django.conf.urls import url

from .views import PlayerView, ManagerView

urlpatterns = [
    url(r'^manage', ManagerView.as_view(), name='manager'),
    url(r'^', PlayerView.as_view(), name='player'),
]
