from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_filter = ["staff"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Other info",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "age",
                    "vision_credits",
                    "currency_type",
                    "gender_type",
                    "country",
                    "adult",
                    "superuser",
                    "staff"
                ],
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "fields": [
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ]
            },
        ), ]
