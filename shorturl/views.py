from django.shortcuts import render
from django.http import HttpResponseRedirect
from shorturl.models import Url_match
from .url_validator import is_valid_url as vu, make_valid_short_url as vsu
from django.shortcuts import get_object_or_404
from django.http import Http404


# Create your views here.
def index(request):
    if request.GET.__contains__('long_url'):
        long_url = request.GET.get('long_url')
        if vu(long_url):
            short_url = vsu()
            a = Url_match(long_url=long_url, short_url=short_url)
            a.save()
            data = {'short_url': 'http://127.0.0.1:8000/' + short_url}
            return render(request, "page1/index.html", context=data)
        else:
            data = {'short_url': 'Please check your URL.'}
            return render(request, "page1/index.html", context=data)
    return render(request, "page1/index.html")


def forvarding(request, short_url):
    b = get_object_or_404(Url_match, short_url=short_url)
    b.call_counter = b.call_counter + 1
    long_url = b.long_url
    b.save()
    return HttpResponseRedirect(long_url)


def get_url_call_counter(request):
    if request.GET.__contains__('url'):
        url = request.GET.get('url')
        try:
            a = get_object_or_404(Url_match, short_url=url)
            data = {'number': a.call_counter}
        except Http404:
            data = {'number': 'Url not found'}
        return render(request, "counter/index.html", data)
    return render(request, "counter/index.html")
