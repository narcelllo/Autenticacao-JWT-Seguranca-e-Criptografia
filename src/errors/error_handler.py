from .types.http_unauthorized import HttpUnauthorizedError
from .types.http_bad_request import HttpBedRequestError
from .types.http_not_found import HttpNotFoundError
from src.views.http_types.http_response import HttpResponse

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpUnauthorizedError, HttpBedRequestError, HttpNotFoundError)): 
        return HttpResponse(
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }, status_code = error.status_code
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Error Server",
                "detail": str(error)
            }]
        }
    )