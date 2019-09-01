from django.views.generic import CreateView
from .models import Urlshorter
from .forms import UrlForms
from .shortener import Shorter
from django.shortcuts import render
from django.http import HttpResponseRedirect


class UrlsViews (CreateView):
    model = Urlshorter
    form_class = UrlForms
    template_name = 'main.html'
    context_name = 'link'

    def post(self, request):
        form = self.form_class(request.POST)
        a = ''
        if form.is_valid():
            new_url = form.save(commit=True)
            a = Shorter().issue()
            new_url.url_short = a
            new_url.save()
            return HttpResponseRedirect('/')
        else:
            form = UrlForms
            a = 'invalid url'

        return render(request, {'form': form, 'a': a})

    def get(request, token):
        long_url = Urlshorter.objects.filter(url_short=token)
        return render(request, long_url.url_long())
