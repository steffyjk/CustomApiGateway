import time
import redis
from fastapi import HTTPException, status
from app.config import REDIS_HOST, REDIS_PORT, RATE_LIMIT_PER_MINUTE

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

def rate_limit(partner_id: str):
    current_minute = int(time.time() / 60)
    key = f"rate:{partner_id}:{current_minute}"

    count = redis_client.incr(key)
    if count == 1:
        redis_client.expire(key, 60)

    if count > RATE_LIMIT_PER_MINUTE:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded"
        )
