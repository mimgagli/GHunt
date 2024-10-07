import httpx
import asyncio

import sys

from ghunt.helpers.gmail import is_email_registered


async def main():
    if not sys.argv[1:]:
        exit("alighieridante33@gmail.com")

    as_client = httpx.AsyncClient() # Async Client

    email = sys.argv[1]
    is_registered = await is_email_registered(as_client, email)

    print("Registered on Google :", is_registered)

asyncio.run(main()) # running our async code in a non-async code
