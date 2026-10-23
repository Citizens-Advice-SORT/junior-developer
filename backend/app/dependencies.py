from fastapi import Request
from gliner2 import GLiNER2


def get_model(request: Request) -> GLiNER2:
    """The redaction model loaded at startup. Use it in an endpoint with Depends(get_model)."""
    return request.app.state.model
