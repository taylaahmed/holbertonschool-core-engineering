#!/usr/bin/env python3

import asyncio
from websockets.asyncio.server import serve, broadcast
from websockets.exceptions import ConnectionClosed


CONNECTED = set()


async def echo(websocket):
    CONNECTED.add(websocket)
    try:
        async for message in websocket:
            broadcast(CONNECTED, f"B:{message}")
    except ConnectionClosed:
        pass
    finally:
        CONNECTED.discard(websocket)


async def main():
    server = await serve(echo, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
