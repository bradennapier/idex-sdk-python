import aiohttp
import asyncio

class IDEXAsyncRequest():
    
  async def create(self):
    async with aiohttp.ClientSession() as session:
        self._session = session
  
  async def post(self):
    pass

  async def get(self):
    pass

  async def delete(self):
    pass

  async def patch(self):
    pass