from django.http import HttpResponse
from .models import Order, OrderLineItem
from packs.models import Pack
import json


class StripeWH_Handler:
    # This class will handle any Stripe Webhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # This function will handle any webhooks that are unexpected
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        # This function will handle any successful webhooks
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total = round(intent.data.charges[0].amount / 100, 2)
        # Ensure every field in shipping_details has a value, or None
        # This is because "" != None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details,
                    street_address2__iexact=shipping_details.name,
                    town_or_city__iexact=shipping_details.name,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    total=total,
                )
                order_exists = True
                break
                return HttpResponse(
                    content=f'Successful Webhook received {event["type"]} | SUCCESS:\
                        Verified order already in data', status=200)
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(content=f'Webhook received: {event["type"]}\
                | SUCCESS: Created order in webhook', status=200)
        else:
            order = None
            try:
                order = Order.Objects.create(
                    full_name=shipping_details.name,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details,
                    street_address2=shipping_details.name,
                    town_or_city=shipping_details.name,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                )
                for item_id, quantity in json.loads(bag).items():
                    pack = Pack.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        pack=pack,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]}\
                    | ERROR: {e}', status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS:\
                Created order in webhook', status=200)

    def handle_payment_intent_failed(self, event):
        # This function will handle any failed webhooks
        return HttpResponse(
            content=f'Webhook received {event["type"]}', status=200)
