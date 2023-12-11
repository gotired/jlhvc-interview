import asyncio
import websockets
import json
import ssl

uri = "wss://api.bitkub.com/websocket-api/market.ticker.thb_btc"

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def do_something_with_message(message):
    data = json.loads(message)
    print("Received message:", data)

async def subscribe_to_websocket():
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        while True:
            try:
                message = await websocket.recv()
                await do_something_with_message(message)
            except websockets.exceptions.ConnectionClosed as e:
                print(f"Connection closed: {e}")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(subscribe_to_websocket())
