from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render

from .forms import ContextForm, PasswordForm
from .models import Context, Quest

class PlayerView(View):
    """ the view of the players """
    template_name_password = 'main/password.html'
    template_name_no_quest = 'main/noquest.html'
    template_name_secret = 'main/secret.html'
    template_name_hacking = 'main/hacking.html'

    hack_pass = 'hack'

    def dispatch(self, request, *args, **kwargs):
        self.game_context = Context.get_instance()
        self.quest = self.game_context.quest
        if self.quest is None:
            return render(request, self.template_name_no_quest)
        elif self.game_context.state == Context.PASSWORD:
            if request.method == 'POST':
                return self.process_password(request, *args, **kwargs)
            else:
                return self.ask_password(request, *args, **kwargs)
        elif self.game_context.state == Context.HACKING:
            if request.method == 'POST':
                return self.process_hacking_success(request, *args, **kwargs)
            else:
                return self.give_hacking_page(request, *args, **kwargs)
        elif self.game_context.state == Context.SUCCESS:
            return self.show_secret_reward(request, *args, **kwargs)
            ward(request, *args, **kwargs)
        else:
            return HttpResponse("Error: invalid context state")

    def process_password(self, request, *args, **kwargs):
        form = PasswordForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            if self.quest.quest_type == Quest.HACK:
                if password == self.hack_pass:
                    self.game_context.state = Context.HACKING
                    self.game_context.save()
                    return self.give_hacking_page(request, *args, **kwargs)

            elif self.quest.password == password:
                self.game_context.state = Context.SUCCESS
                self.game_context.save()
                return self.show_secret_reward(request, *args, **kwargs)

        return self.ask_password(request, *args, **kwargs)

    def ask_password(self, request, *args, **kwargs):
        form = PasswordForm()
        context = {
            'form': form,
            'enigma': self.quest.enigma if self.quest.quest_type == Quest.ENIGMA
                else None
        }
        return render(request, self.template_name_password, context)

    def give_hacking_page(self, request, *args, **kwargs):
        context = {
            'mini_game': self.quest.mini_game,
        }
        return render(request, self.template_name_hacking, context)

    def process_hacking_success(self, request, *args, **kwargs):
        if request.POST.has_key('result') and request.POST['result'] == 'success':
            self.game_context.state = Context.SUCCESS
            self.game_context.save()
            return self.show_secret_reward(request, *args, **kwargs)
        else:
            return self.give_hacking_page(request, *args, **kwargs)

    def show_secret_reward(self, request, *args, **kwargs):
        context = {
            'secret': self.quest.secret,
        }
        return render(request, self.template_name_secret, context)


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
