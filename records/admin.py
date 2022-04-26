from django.contrib import admin
from .models import UserTeam,Player,Team,Contest
# Register your models here.

models = [UserTeam,Player,Team,Contest]

for model in models:
    admin.site.register(model)