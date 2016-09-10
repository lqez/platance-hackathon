from django.conf import settings


def api_key(request):
    print settings.GOOGLE_API_KEY
    return {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
    }
