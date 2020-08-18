from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler
import stripe


# The core of this webhook code can be found at :
# https://stripe.com/docs/payments/handling-payment-events
@require_POST
@csrf_exempt
def my_webhook_view(request):
    # Setup Our Webhook Keys
    endpoint_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # Handle and verify the data
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up Webhook Handler
    handler = StripeWH_Handler(request)
    # Allocate events to specific handling functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }
    # Get Webhook Type from Stripe
    event_type = event['type']
    # Associate with event_map
    event_handler = event_map.get(event_type, handler.handle_event)
    # Generate response with event_handler
    response = event_handler(event)
    return response
