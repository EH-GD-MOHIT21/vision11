from django.shortcuts import redirect, render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from payments.repository import vision11_payments
from .models import Plan, Order
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework.views import APIView



# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))




@login_required(login_url='/accounts/login')
def render_offer_page(request):
    if not request.user.is_adult or request.user.currency_type=='vision candies':
        return HttpResponseBadRequest('please verify you are 18+ year old.')
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
    return render(request, 'offers.html', {'plans': zip(render_this, show_banner)})




@login_required(login_url='/accounts/login')
def homepage(request, offerid):
    if not request.user.is_adult or request.user.currency_type=='vision candies':
        return HttpResponseBadRequest('please verify you are 18+ year old.')
    currency = 'INR'
    try:
        plan = Plan.objects.get(id=offerid)
        if plan.offer_end_date == '' or plan.offer_end_date == None:
            pass
        elif timezone.now() > plan.offer_end_date:
            return HttpResponseBadRequest()
    except Exception as e:
        return HttpResponseBadRequest()
    amount = plan.plan_price * 100  # to paise

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['plan'] = plan
    try:
        Order.objects.get(user=request.user,
                          amount=plan.plan_price, order_id=razorpay_order_id)
    except:
        Order.objects.create(
            user=request.user, amount=plan.plan_price, order_id=razorpay_order_id,plan_benefits=plan.vision_coins).save()

    return render(request, 'razorpay.html', context=context)






# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@login_required(login_url='/accounts/login')
@csrf_exempt
def paymenthandler(request):
    if not request.user.is_adult or request.user.currency_type=='vision candies':
        return HttpResponseBadRequest('please verify you are 18+ year old.')
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            order = Order.objects.get(order_id=razorpay_order_id)
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result:
                amount = order.amount * 100
                try:
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    order.update_status
                    
                    request.user.vision_credits += round(order.plan_benefits,3)
                    request.user.save()
                    order.save()
                    # render success page on successful caputre of payment
                    return redirect('/')
                except:
                    # if there is an error while capturing payment.
                    return HttpResponseBadRequest()
            else:
                # if signature verification fails.
                return HttpResponseBadRequest()
        except:
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()



class GetOfferListAPI(APIView):
    def get(self,request):
        try:
            if request.user.is_authenticated and request.user.is_adult:
                return vision11_payments().get_offer_list()
            return Response({'status':403,'message':'You aren\'t adult or authorised.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})