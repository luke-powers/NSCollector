from django.views import generic
from .models import Census, CensusChangesLog



class IndexView(generic.ListView):
    template_name = 'census/index.html'
    context_object_name = 'census_list'

    def get_queryset(self):
        return Census.objects.all()

class AddView(generic.edit.CreateView):
    model = CensusChangesLog
    form_class = CensusChangesLogForm
    template_name = 'census/edit.html'
    success_url = ''
