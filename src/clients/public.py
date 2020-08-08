import aiohttp
import asyncio

from src.config import APIConfig
from src.async_request import IDEXAsyncRequest

class PublicClient():
    def __init__(self, config: APIConfig):
        print('config', config)
        self.config = config

    async def create(self, is_sandbox: bool):
        self.request = IDEXAsyncRequest()
        await self.request.create()

    async def get_ping(self):
        """
          https://docs.idex.io/#get-ping
        """
        pass

    async def get_server_time(self):
        """
          https://docs.idex.io/#get-time
        """
        pass

    async def get_exchange(self):
        """
          https://docs.idex.io/#get-exchange
        """
        pass

    async def get_assets(self):
        """
          https://docs.idex.io/#get-assets
        """
        pass

    async def get_markets(self):
        """
          https://docs.idex.io/#get-markets
        """
        pass

    async def get_tickers(self):
        """
          https://docs.idex.io/#get-tickers
        """
        pass

    async def get_candles(self):
        """
          https://docs.idex.io/#get-candles
        """
        pass

    async def get_trades(self):
        """
          https://docs.idex.io/#get-trades
        """
        pass

    async def get_order_book_l1(self):
        """
          https://docs.idex.io/#get-order-books
        """
        pass

    async def get_order_book_l2(self):
        """
          https://docs.idex.io/#get-order-books
        """
        pass
