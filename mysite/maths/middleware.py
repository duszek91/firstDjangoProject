# https://docs.djangoproject.com/en/3.2/topics/http/middleware/
# https://stackoverflow.com/questions/33314717/how-to-understand-tornado-response-request-cycle-in-django
from django.http import HttpResponseForbidden

from django.utils import timezone


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response
        
    return middleware