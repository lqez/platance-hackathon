from django.conf import settings


def api_key(request):
    return {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
    }
