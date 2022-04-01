from django.shortcuts import redirect, render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .models import Plan,Order
from django.contrib.auth.decorators import login_required


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


@login_required(login_url='/accounts/login')
def render_offer_page(request):
	plans = Plan.objects.all()
	return render(request,'offers.html',{'plans':plans})


@login_required(login_url='/accounts/login')
def homepage(request,offerid):
	currency = 'INR'
	try:
		plan = Plan.objects.get(id=offerid)
	except:
		return HttpResponseBadRequest()
	amount = plan.plan_price * 100 # to paise
 
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
		Order.objects.get(user=request.user,amount=plan.plan_price,order_id=razorpay_order_id)
	except:
		Order.objects.create(user=request.user,amount=plan.plan_price,order_id=razorpay_order_id).save()
 
	return render(request, 'razorpay.html', context=context)



# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@login_required(login_url='/accounts/login')
@csrf_exempt
def paymenthandler(request):
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