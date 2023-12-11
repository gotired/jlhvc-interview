import hashlib
import hmac
from dotenv import load_dotenv
import os

load_dotenv()


def gen_sign(api_secret, payload_string=None):
    return hmac.new(
        api_secret.encode("utf-8"), payload_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()


Config = {
    "host": "https://api.bitkub.com",
    "path": {
        "sell": "/api/v3/market/place-ask",
        "buy": "/api/v3/market/place-bid",
        "cancel": "/api/v3/market/cancel-order",
    },
    "api_key": os.getenv("API_KEY"),
    "api_secret": os.getenv("API_SECRET"),
}
