from tastypie.resources import ModelResource
from .models import Census


class CensusResource(ModelResource):
    class Meta:
        queryset = Census.objects.all()
        resource_name = 'census'
