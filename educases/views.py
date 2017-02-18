from django.views import generic
from .models import Subject, Science, Economy, Art


class IndexView(generic.ListView):
    template_name = 'educases/index.html'
    context_object_name = 'all_subjects'
    subjects = Subject.objects.all()
    sciences = Science.objects.all()
    economics = Economy.objects.all()
    arts = Art.objects.all()

    def get_queryset(self):
        return self.sciences, self.economics, self.arts


class DetailView(generic.DetailView):
    model = Subject
    template_name = 'educases/details.html'


def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
