import re, random, string
from django.core.exceptions import ObjectDoesNotExist
from shorturl.models import Url_match
from django.core.validators import URLValidator
from django.core.validators import ValidationError


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False


def is_valid_short_url():
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    try:
        Url_match.objects.get(short_url=short_url)
        is_valid_short_url()
    except ObjectDoesNotExist:
        return short_url
