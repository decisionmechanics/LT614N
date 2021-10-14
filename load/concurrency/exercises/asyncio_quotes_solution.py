import aiohttp
import asyncio
import json
import sys
import time

INSPIRATIONAL_QUOTES_URL = (
    "https://inspirational-quotes.azurewebsites.net/api/InspirationalQuotes"
)


async def fetch_quote(url, session):
    async with session.get(url) as response:
        text = await response.text()
        return json.loads(text)


async def fetch_quotes(n):
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(
            *(fetch_quote(INSPIRATIONAL_QUOTES_URL, session) for _ in range(n))
        )


async def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    start_time = time.perf_counter()

    quotes = await fetch_quotes(n)

    duration = time.perf_counter() - start_time

    for quote in quotes:
        text = quote["text"].strip("“")

        print(f'"{text}" -- {quote["from"]}')

    print(f"Fetched {n} inspirational quote(s) in {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
