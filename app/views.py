from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse
from app.models import Text

from app import services


class TextListView(ListView):
    template_name = 'list.html'
    model = Text


class TextCreateView(CreateView):
    template_name = 'create.html'
    model = Text
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save()
        services.analyzer(self.object)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('texts:detail', args=(self.object.id,))


class TextDetailView(DetailView):
    template_name = 'detail.html'
    model = Text
