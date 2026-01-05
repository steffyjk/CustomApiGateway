import time
from fastapi import FastAPI, Depends, Request
from app.auth import verify_api_key
from app.rate_limiter import rate_limit
from app.proxy import proxy_request
from app.logger import log_request

app = FastAPI(title="API Gateway")

ALLOWED_PATHS = {
    "users",
    "posts",
    "comments",
    "albums",
    "photos",
    "todos"
}

@app.api_route("/{path:path}", methods=["GET"])
async def gateway(
    path: str,
    request: Request,
    api_key: str = Depends(verify_api_key)
):
    if path not in ALLOWED_PATHS:
        return {"error": "Invalid endpoint"}

    start_time = time.time()

    # Rate limit
    rate_limit(api_key)

    # Forward request
    response = await proxy_request(request, path)

    duration = int((time.time() - start_time) * 1000)
    log_request(api_key, path, request.method, response.status_code, duration)

    return response
