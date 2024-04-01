from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from course.models import Course

from django.views.generic.base import TemplateView
from django.contrib import messages
import stripe

class HomePageView(TemplateView):
    template_name = 'payments/home.html'

class SuccessView(TemplateView):
    template_name = 'payments/success.html'

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        course = get_object_or_404(Course, slug=slug)
        user = request.user
        course.students.add(user)
        messages.success(request, f"Payment successful! You've successfully enrolled in {course.title}. Enjoy learning!")
        return redirect('course:detail', slug=slug)
    
class CancelledView(TemplateView):
    template_name = 'payments/cancelled.html'
    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        course = get_object_or_404(Course, slug=slug)
        messages.error(request, "Payment Unsuccessful.")
        # Redirect to the course page
        return redirect('course:overview', slug=slug)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    
@csrf_exempt
def create_checkout_session(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url +'/payments/'+ slug + '/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url +'/payments/'+ slug + '/payments/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price_data': {
                            'currency': 'kes',
                            'unit_amount': int(course.price*100),
                            'product_data': {
                                'name': course.title,
                            },
                        },
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})