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
          {
              "depositEnabled": true,
              "orderEnabled": true,
              "cancelEnabled": true,
              "withdrawEnabled": true,
              "kycTier": 2,
              "totalPortfolioValueUsd": "127182.82",
              "withdrawalLimit": "unlimited",
              "withdrawalRemaining": "unlimited",
              "makerFeeRate": "0.001",
              "takerFeeRate": "0.002"
          }
        """
        pass

    async def associate_wallet(self, nonce, wallet):
        """
          https://docs.idex.io/#associate-wallet
          {
              "address": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
              "totalPortfolioValueUsd": "88141.77",
              "time": 1590393600000
          }
        """
        pass

    async def get_wallets(self, nonce):
        """
          https://docs.idex.io/#get-wallets
          [
              {
                  "address": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
                  "totalPortfolioValueUsd": "88141.77",
                  "time": 1590393600000
              },
              ...
          ]
        """
        pass

    async def get_balances(self):
        """
          https://docs.idex.io/#get-balances
          [
              {
                  "asset": "USDC",
                  "quantity": "38192.94678100",
                  "availableForTrade": "26710.66678121",
                  "locked": "11482.28000000",
                  "usdValue": "38188.22"
              },
              ...
          ]
        """
        pass

    async def create_order(self):
        """
          https://docs.idex.io/#create-order
          
          # Example Market Order Request
          
          {
              "parameters": {
                  "nonce": "8fa5dce0-9ee6-11ea-9fa0-bf38ac8631c1",
                  "wallet": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
                  "market": "ETH-USDC",
                  "type": "market",
                  "side": "buy",
                  "quoteOrderQuantity": "1000.00000000"
                },
              "signature": "<Ethereum wallet signature>"
          }

          {
                "market": "ETH-USDC",
                "orderId": "92782120-a775-11ea-aa55-4da1cc97a06d",
                "wallet": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
                "time": 1590394200000,
                "status": "filled",
                "type": "market",
                "side": "buy",
                "originalQuoteQuantity": "1000.00000000",
                "executedQuantity": "4.95044603",
                "cumulativeQuoteQuantity": "1000.00000000",
                "avgExecutionPrice": "202.00200000",
                "fills": [
                    {
                        "fillId": "974480d0-a776-11ea-895b-bfcbb5bdaa50",
                        "price": "202.00150000",
                        "quantity": "3.78008801",
                        "quoteQuantity": "763.58344815",
                        "time": 1590394200000,
                        "makerSide": "sell",
                        "sequence": 981372,
                        "fee": "0.00756017",
                        "feeAsset": "ETH",
                        "liquidity": "taker",
                        "txId": "0x01d28c33271cf1dd0eb04249617d3092f24bd9bad77ffb57a0316c3ce5425158",
                        "txStatus": "mined"
                    },
                    ...
                ]
            }
            
            # Example Stop Loss Limit Request 
            {
                "parameters": {
                    "nonce": "dd2e0930-a777-11ea-b5e9-d9c1e499360f",
                    "wallet": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
                    "market": "ETH-USDC",
                    "type": "stopLossLimit",
                    "side": "sell",
                    "quantity": "4.95044603",
                    "price": "190.00000000",
                    "stopPrice": "195.00000000",
                    "clientOrderId": "199283"
                  },
                "signature": "<Ethereum wallet signature>"
            }
            
            {
                "market": "ETH-USDC",
                "orderId": "3a9ef9c0-a779-11ea-907d-23e999279287",
                "clientOrderId": "199283",
                "wallet": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
                "time": 1590394500000,
                "status": "active",
                "type": "stopLossLimit",
                "side": "sell",
                "originalQuantity": "4.95044603",
                "executedQuantity": "0.00000000",
                "cumulativeQuoteQuantity": "0.00000000",
                "price": "190.00000000",
                "stopPrice": "195.00000000"
            }
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
          
          {
              "parameters": {
                  "nonce": "91f460c0-9ee6-11ea-9026-c1542192a384",
                  "wallet": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
                  "orderId": "3a9ef9c0-a779-11ea-907d-23e999279287"
              },
              "signature": "<Ethereum wallet signature>"
          }
          
          [
              {
                  "orderId": "3a9ef9c0-a779-11ea-907d-23e999279287"
              },
              ...
          ]
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
          
          [
            {
                "fillId": "974480d0-a776-11ea-895b-bfcbb5bdaa50",
                "price": "202.00150000",
                "quantity": "3.78008801",
                "quoteQuantity": "763.58344815",
                "time": 1590394200000,
                "makerSide": "sell",
                "sequence": 981372,
                "market": "ETH-USDC",
                "orderId": "92782120-a775-11ea-aa55-4da1cc97a06d",
                "side": "buy",
                "fee": "0.00756017",
                "feeAsset": "ETH",
                "liquidity": "taker",
                "txId": "0x01d28c33271cf1dd0eb04249617d3092f24bd9bad77ffb57a0316c3ce5425158",
                "txStatus": "mined"
            },
            ...
          ]
        """
        pass

    async def get_deposit(self):
        """
          https://docs.idex.io/#get-deposits
          
          [
              {
                  "depositId": "57f88930-a6c7-11ea-9d9c-6b2dc98dcc67",
                  "asset": "USDC",
                  "quantity": "25000.00000000",
                  "txId": "0xf3299b8222b2977fabddcf2d06e2da6303d99c976ed371f9749cb61514078a07",
                  "txTime": 1590393900000,
                  "confirmationTime": 1590394050000
              },
              ...
          ]
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
          
          {
              "parameters": {
                  "nonce": "93dd1df0-9ee6-11ea-a40b-3148146b6ce3",
                  "wallet": "0xA71C4aeeAabBBB8D2910F41C2ca3964b81F7310d",
                  "asset": "USDC",
                  "quantity": "1000.00000000"
              },
              "signature": "<Ethereum wallet signature>"
          }
          
          [
              {
                  "withdrawalId": "3ac67790-a77c-11ea-ae39-b3356c7170f3",
                  "asset": "USDC",
                  "assetContractAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                  "quantity": "25000.00000000",
                  "time": 1590394800000,
                  "fee": "0.14332956",
                  "txId": "0xf215d7a6d20f6dda52cdb3a3332aa5de898dead06f92f4d26523f140ae5dcc5c",
                  "txStatus": "mined"
              },
              ...
          ]
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
          
          {
              "token": "<WebSocket authentication token>"
          }
        """
        pass
