from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def get_sample(r: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status=200,
        content=b'sample content'
    )
