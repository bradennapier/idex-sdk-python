import aiohttp
import asyncio

import urllib

from .config import APIConfig


class IDEXAsyncRequest():

    async def create(self):
        async with aiohttp.ClientSession() as session:
            self._session = session

    def _prepare_request(self, *, config: APIConfig, params=None):
        options = {
            'base_url': config.get_rest_url(),
            'headers': config.get_headers()
        }

        if params != None:
            options['headers'] = config.get_headers(
                params=urllib.parse.urlencode(params)
            )
        else:
            options['headers'] = config.get_headers()

        return options

    async def post(self):
        pass

    async def get(self):
        pass

    async def delete(self):
        pass

    async def patch(self):
        pass
