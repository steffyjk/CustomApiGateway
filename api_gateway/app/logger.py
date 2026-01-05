import time

def log_request(partner_id, path, method, status_code, duration):
    print({
        "partner": partner_id,
        "path": path,
        "method": method,
        "status": status_code,
        "response_time_ms": duration
    })
