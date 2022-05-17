from django.contrib import admin
from .models import Plan, Order
# Register your models here.

class CustomPlan(admin.ModelAdmin):
    list_display = ["plan_price","vision_coins","bonus_coins","offer_start_date","offer_end_date"]
    search_fields = ["plan_price","vision_coins","bonus_coins","offer_start_date","offer_end_date"]



class CustomOrder(admin.ModelAdmin):
    list_display = ["user","order_id","order_status","amount","currency"]
    search_fields = ["user__username","user__email","order_id","order_status"]


admin.site.register(Plan,CustomPlan)
admin.site.register(Order,CustomOrder)
