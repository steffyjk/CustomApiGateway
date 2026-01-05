import httpx
from fastapi import Request, Response
from app.config import BACKEND_BASE_URL

EXCLUDED_HEADERS = {
    "host",
    "authorization",
    "x-api-key",
    "content-length"
}

async def proxy_request(request: Request, path: str):
    url = f"{BACKEND_BASE_URL}/{path}"

    # Filter headers
    headers = {
        k: v for k, v in request.headers.items()
        if k.lower() not in EXCLUDED_HEADERS
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.request(
            method=request.method,
            url=url,
            params=request.query_params,
            headers=headers
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("content-type")
    )
