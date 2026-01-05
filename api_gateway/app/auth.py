from fastapi import Header, HTTPException, status

# Dummy API keys (replace with DB later)
VALID_API_KEYS = {
    "partner_123": "Partner A",
    "partner_456": "Partner B",
}

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return x_api_key
