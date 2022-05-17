from django.contrib import admin
from chatsupportAPP.models import Chat, Queue
# Register your models here.


class CustomChat(admin.ModelAdmin):
    list_display = ["user","group","timestamp"]
    search_fields = ["user__username","user__email","group","timestamp"]


class CustomQueue(admin.ModelAdmin):
    list_display = ["user","group_name","joined_at"]
    search_fields = ["user__username","user__email","group_name","joined_at"]


admin.site.register(Chat,CustomChat)
admin.site.register(Queue,CustomQueue)