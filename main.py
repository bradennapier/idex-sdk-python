# example import
import asyncio

from web3 import Web3
from web3.auto import w3

from src.config import APIConfig
from src.clients.public import PublicClient

async def main():
    config = APIConfig(
        api_key='<api_key>',
        api_secret='<api_secret>',
        # These values are provided as arguments so that web3 won't have to be
        # a dependency of the api wrapper itself.  This may be fine, not sure if 
        # there are other packages that may be desired instead to do these things
        solidityKeccak=Web3.solidityKeccak,
        ethSignMessage=w3.eth.account.sign_message
    )
    client = PublicClient(
        config=config
    )
    await client.create(True)
    
  
asyncio.run(main())
