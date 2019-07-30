from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from shorturl.models import Url_match
import random, string
from .url_validator import is_valid_url as vu


# Create your views here.
def main_page(request):
    if request.GET.getlist('long_url'):
        long_url = str(request.GET.getlist('long_url')[0])
        if vu(long_url):
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            a = Url_match(long_url=long_url, short_url=short_url)
            a.save()
            data = {'short_url': 'http://127.0.0.1:8000/' + short_url}
            return render(request, "page1/index.html", context=data)
        else:
            data = {'short_url': 'Please check your URL.'}
            return render(request, "page1/index.html", context=data)
    return render(request, "page1/index.html")


def forvarding(request):
    short_url = ''.join(HttpRequest.get_full_path(request)[1:-1])
    long_url = str(Url_match.objects.filter(short_url=short_url)[0])
    return HttpResponseRedirect(long_url)
