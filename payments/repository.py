from .models import Plan
from django.utils import timezone
from rest_framework.response import Response
from .serializers import PlanSerializer

class vision11_payments:

    def get_offer_list(self):
        plans = Plan.objects.all()
        render_this = []
        show_banner = []
        for plan in plans:
            if plan.offer_end_date == None or plan.offer_end_date == '':
                render_this.append(plan)
                show_banner.append(False)
            elif plan.offer_end_date > timezone.now():
                render_this.append(plan)
                t = plan.offer_end_date - timezone.now()
                show_banner.append(t.days*24*60*60+t.seconds)
        serializer = PlanSerializer(render_this,many=True)
        return Response({'status':200,'plans': serializer.data,'banner': show_banner,'message':'success'})