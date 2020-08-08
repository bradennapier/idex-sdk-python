import asyncio
from src.config import APIConfig
from src.async_request import IDEXAsyncRequest

class AuthenticatedClient():
    def __init__(self, config: APIConfig):
        print('config', config)
        self.config = config
        
    async def create(self, is_sandbox: bool):
        self.request = IDEXAsyncRequest()
        await self.request.create()

    async def get_user(self, nonce):
        """
          https://docs.idex.io/#get-user-account
        """
        pass

    async def get_wallets(self, nonce):
        """
          https://docs.idex.io/#get-wallets
        """
        pass

    async def get_balances(self):
        """
          https://docs.idex.io/#get-balances
        """
        pass

    async def associate_wallet(self):
        """
          https://docs.idex.io/#associate-wallet
        """
        pass

    async def create_order(self):
        """
          https://docs.idex.io/#create-order
        """
        pass

    async def create_test_order(self):
        """
          https://docs.idex.io/#test-create-order
        """
        pass

    async def cancel_order(self):
        """
          https://docs.idex.io/#cancel-order
        """
        pass

    async def cancel_orders(self):
        """
          https://docs.idex.io/#cancel-order
        """
        pass

    async def get_order(self):
        """
          https://docs.idex.io/#get-orders
        """
        pass

    async def get_orders(self):
        """
          https://docs.idex.io/#get-orders
        """
        pass

    async def get_fill(self):
        """
          https://docs.idex.io/#get-fills
        """
        pass

    async def get_fills(self):
        """
          https://docs.idex.io/#get-fills
        """
        pass

    async def get_deposit(self):
        """
          https://docs.idex.io/#get-deposits
        """
        pass

    async def get_deposits(self):
        """
          https://docs.idex.io/#get-deposits
        """
        pass

    async def withdraw(self):
        """
          https://docs.idex.io/#withdraw-funds
        """
        pass

    async def get_withdrawal(self):
        """
          https://docs.idex.io/#get-withdrawals
        """
        pass

    async def get_withdrawals(self):
        """
          https://docs.idex.io/#get-withdrawals
        """
        pass

    async def get_ws_token(self):
        """
          https://docs.idex.io/#get-authentication-token
        """
        pass
