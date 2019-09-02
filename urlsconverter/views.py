from django.views.generic import CreateView, DetailView
from .models import Urlshorter
from .forms import UrlForms
from .shortener import Shorter
from django.urls import reverse


class UrlsViews (CreateView):
    model = Urlshorter
    form_class = UrlForms
    template_name = 'main.html'

    def form_valid(self, form):
        new_url = form.save(commit=True)
        a = Shorter().issue()
        new_url.url_short = a
        new_url.save()
        form.instance.url = new_url
        return super(UrlsViews, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class UrlsDetailView(DetailView):
    model = Urlshorter
    context_object_name = 'link'
    template_name = 'detail.html'
    pk_url_kwarg = 'link_id'


