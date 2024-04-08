from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription
from services.serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client',
        queryset=Client.objects.all().select_related('user').only('company_name', 'user__email'))
    ).annotate(price=F('services.service.full_price')-F('services.service.full_price')*F('services.plan.discount_percent')/100)
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        response = super.list(request, *args, **kwargs)
        response_data = {'result' : response.data}
        response_data['total_amount'] = self.queryset.aggregate(total=Sum('price')).get('total')
        response_data = response_data

        return response

