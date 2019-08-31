from django.views import View
from .models import Urlshorter
from .forms import UrlForms
from .shortener import Shorter
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


class UrlsViews (View):
    model = Urlshorter
    form_class = UrlForms
    template_name = 'main.html'

    def post(self, request):
        form = self.form_class(request.POST)
        a = ''
        if form.is_valid():
            new_url = form.save(commit=False)
            a = Shorter().issue()
            new_url.url_short = a
            new_url.save()
            # return HttpResponseRedirect('/success/')
        else:
            form = UrlForms
            a = 'invalid url'

        return render(request, self.template_name, {'form': form, 'a': a})

    def get(request, token):
        long_url = Urlshorter.objects.filter(url_short=token)[0]
        return redirect(long_url.url_long())
