from django.http import HttpResponse


class StripeWH_Handler:
    """ This will handle any Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ This function will handle any webhooks that are unexpected """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """ This function will handle any successful webhooks"""
        return HttpResponse(
            content=f'Successful Webhook received {event["type"]}', status=200)

    def handle_payment_intent_failed(self, event):
        """ This function will handle any failed webhooks"""
        return HttpResponse(
            content=f'Webhook received {event["type"]}', status=200)
