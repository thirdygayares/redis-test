import redis.asyncio as redis
import asyncio

async def main():
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)

    await r.set("name", "Thirdy Gayares")
    val = await r.get("name")
    print(val)

asyncio.run(main())