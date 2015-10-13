from django.http import HttpResponse
from django.views.generic import View, TemplateView

from .forms import ContextForm
from .models import Context

class PlayerView(View):
    """ the view of the players """

    def get(self, request, *args, **kwargs):
        return HttpResponse("PlayerView")


class ManagerView(TemplateView):
    """ the view of the managers """

    template_name = 'main/manager.html'
    form_class = ContextForm

    def get_context_data(self, **kwargs):
        context = super(ManagerView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        self.form = self.form_class(instance=Context.get_instance())
        return super(ManagerView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST, instance=Context.get_instance())
        if self.form.is_valid():
            context = self.form.save(commit=False)
            if context.quest is None:
                context.state = None
            else:
                context.state = Context.PASSWORD
            context.save()
        return super(ManagerView, self).get(request, *args, **kwargs)
