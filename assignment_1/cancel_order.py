from .config import *
import json
import time
import requests


if __name__ == "__main__":
    ts = str(round(time.time() * 1000))

    if len(sys.argv) != 4:
        print("Usage: python3 cancel_order.py symbol order_id order_side")
        sys.exit(1)

    symbol = sys.argv[1]
    order_id = sys.argv[2]
    order_side = sys.argv[3]

    reqBody = {"sym": symbol, "id": order_id, "sd": order_side}
    payload = [ts, "POST", Config["path"]["cancel"], json.dumps(reqBody)]

    sig = gen_sign(Config["api_secret"], "".join(payload))
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-BTK-TIMESTAMP": ts,
        "X-BTK-SIGN": sig,
        "X-BTK-APIKEY": Config["api_key"],
    }

    response = requests.request(
        "POST",
        Config["host"] + Config["path"]["cancel"],
        headers=headers,
        data=json.dumps(reqBody),
        verify=False,
    )
