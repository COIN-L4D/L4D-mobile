from django.contrib import admin
from django.db import models

from .models import Context, Quest, MiniGame

class ContextAdmin(admin.ModelAdmin):
    pass

class QuestAdmin(admin.ModelAdmin):
    pass

class MiniGameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Context, ContextAdmin)
admin.site.register(Quest, QuestAdmin)
admin.site.register(MiniGame, MiniGameAdmin)
