import django_filters
from web_app.models import Detail

class DetailFilter(django_filters.FilterSet):
    class Meta:
        model = Detail
        fields = ['name','pet_type','pet_name']
