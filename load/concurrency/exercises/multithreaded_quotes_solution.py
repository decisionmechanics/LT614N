import concurrent.futures
import requests
import sys
import threading
import time

INSPIRATIONAL_QUOTES_URL = (
    "https://inspirational-quotes.azurewebsites.net/api/InspirationalQuotes"
)

thread_local = threading.local()


def get_session():
    """Session is not thread-safe, so each thread needs it's own session."""
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def fetch_quote(url):
    session = get_session()

    with session.get(url) as response:
        return response.json()


def fetch_quotes(n):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        return executor.map(fetch_quote, [INSPIRATIONAL_QUOTES_URL] * n)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    start_time = time.perf_counter()

    quotes = fetch_quotes(n)

    duration = time.perf_counter() - start_time

    for quote in quotes:
        text = quote["text"].strip("“")

        print(f'"{text}" -- {quote["from"]}')

    print(f"Fetched {n} inspirational quote(s) in {duration:.2f} seconds")


if __name__ == "__main__":
    main()
