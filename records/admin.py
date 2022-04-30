from django.contrib import admin
from .models import UserTeam,Player,Contest
# Register your models here.

models = [UserTeam,Player,Contest]

for model in models:
    admin.site.register(model)