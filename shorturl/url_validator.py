import re, random, string
from django.core.exceptions import ObjectDoesNotExist
from shorturl.models import Url_match


def is_valid_url(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if regex.match(url) != None:
        return True
    else:
        return False


def is_valid_short_url():
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    try:
        Url_match.objects.get(short_url=short_url)
        is_valid_short_url()
    except ObjectDoesNotExist:
        return short_url
