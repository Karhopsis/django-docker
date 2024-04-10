import datetime
import time

from celery import shared_task
from celery_singleton import Singleton
from django.db import transaction
from django.db.models import Prefetch, F



@shared_task(base=Singleton)
def set_price(subscription_id):
    with transaction.atomic():
        time.sleep(5)
        from services.models import Subscription
        subscription = Subscription.objects.select_for_update().filter(id=subscription_id).annotate(annotated_price=F('service__full_price') -
                               F('service__full_price')*F('plan__discount_percent')/100.00).first()


        subscription.price = subscription.annotated_price
        subscription.save()

@shared_task(base=Singleton)
def set_comment(subscription_id):
    with transaction.atomic():
        time.sleep(5)
        from services.models import Subscription
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)
        new_comment = str(datetime.datetime.now())

        subscription.comment = new_comment
        subscription.save()