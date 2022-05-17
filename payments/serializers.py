from attr import fields
from rest_framework.serializers import ModelSerializer
from .models import Order, Plan


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"