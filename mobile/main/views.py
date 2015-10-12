from django.http import HttpResponse
from django.views.generic import View

class PlayerView(View):
    """ the view of the players """

    def get(self, request, *args, **kwargs):
        return HttpResponse("PlayerView")


class ManagerView(View):
    """ the view of the managers """

    def get(self, request, *args, **kwargs):
        return HttpResponse("ManagerView")
