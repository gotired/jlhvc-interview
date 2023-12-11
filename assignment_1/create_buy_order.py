from .config import *
import json
import time
import requests
import sys


if __name__ == "__main__":
    ts = str(round(time.time() * 1000))

    if len(sys.argv) != 5:
        print("Usage: python3 create_buy_order.py symbol amount rate order_type")
        sys.exit(1)

    symbol = sys.argv[1]
    amount = sys.argv[2]
    rate = sys.argv[3]
    order_type = sys.argv[4]

    reqBody = {"sym": symbol, "amt": int(amount), "rat": int(rate), "typ": order_type}
    payload = [ts, "POST", Config["path"]["buy"], json.dumps(reqBody)]

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
        Config["host"] + Config["path"]["buy"],
        headers=headers,
        data=json.dumps(reqBody),
        verify=False,
    )
