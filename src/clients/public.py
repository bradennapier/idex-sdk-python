from typing import Optional, Literal, List, Union

# Todo figure out how to fix pylint for importing

from src.config import APIConfig
from src.async_request import IDEXAsyncRequest

Asset = Literal[{
    "name": str,
    "symbol": str,
    "contractAddress": str,
    "assetDecimals": int,
    "exchangeDecimals": 8
}]

Market = Literal[{
    "market": str,
    "status": Union[
        Literal["active"],
        Literal["inactive"],
        Literal["cancelsOnly"],
        Literal["limitMakerOnly"]
    ],
    "baseAsset": str,
    "baseAssetPrecision": 8,
    "quoteAsset": str,
    "quoteAssetPrecision": 8
}]

Exchange = Literal[{
    'timeZone': 'UTC',
    'serverTime': int,
    'ethereumDepositContractAddress': str,
    'ethUsdPrice': str,
    'gasPrice': str,
    'volume24hUsd': str,
    'makerFeeRate': str,
    'takerFeeRate': str,
    'makerTradeMinimum': str,
    'takerTradeMinimum': str,
    'withdrawalMinimum': str
}]


class PublicClient():
    def __init__(self, config: APIConfig):
        print('config', config)
        self.config = config

    async def create(self):
        self.request = IDEXAsyncRequest()
        await self.request.create()

    async def get_ping(self) -> Literal[{}]:
        """
          https://docs.idex.io/#get-ping.
          {}
        """
        pass

    async def get_server_time(self) -> Literal[{
        'serverTime': int
    }]:
        """
          https://docs.idex.io/#get-time
          {
            "serverTime": 1590408000000
          }
        """
        pass

    async def get_exchange(self) -> Exchange:
        """
          https://docs.idex.io/#get-exchange
          {
            "timeZone": "UTC",
            "serverTime": 1590408000000,
            "ethereumDepositContractAddress": "0x...",
            "ethUsdPrice": "206.46",
            "gasPrice": 7,
            "volume24hUsd": "10416227.98",
            "makerFeeRate": "0.001",
            "takerFeeRate": "0.002",
            "makerTradeMinimum": "0.15000000",
            "takerTradeMinimum": "0.05000000",
            "withdrawalMinimum": "0.04000000"
          }
        """
        pass

    async def get_assets(self) -> List[Asset]:
        """
          https://docs.idex.io/#get-assets
          [
              {
                  "name": "Ethereum",
                  "symbol": "ETH",
                  "contractAddress": "0x0000000000000000000000000000000000000000",
                  "assetDecimals": 18,
                  "exchangeDecimals": 8
              },
              {
                  "name": "USD Coin",
                  "symbol": "USDC",
                  "contractAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                  "assetDecimals": 6,
                  "exchangeDecimals": 8
              },
              ...
          ]
        """
        pass

    async def get_markets(self) -> List[Market]:
        """
          https://docs.idex.io/#get-markets
          [
              {
                  "market": "ETH-USDC",
                  "status": "active",
                  "baseAsset": "ETH",
                  "baseAssetPrecision": 8,
                  "quoteAsset": "USDC",
                  "quoteAssetPrecision": 8
              },
              ...
          ]
        """
        pass

    async def get_tickers(self):
        """
          https://docs.idex.io/#get-tickers
          [
              {
                  "market": "ETH-USDC",
                  "time": 1590408000000,
                  "open": "202.11928302",
                  "high": "207.58100029",
                  "low": "201.85600392",
                  "close": "206.00192301",
                  "closeQuantity": "9.50000000",
                  "baseVolume": "11297.01959248",
                  "quoteVolume": "2327207.76033252",
                  "percentChange": "1.92",
                  "numTrades": 14201,
                  "ask": "206.00207150",
                  "bid": "206.00084721",
                  "sequence": 848728
              },
              ...
          ]
        """
        pass

    async def get_candles(self):
        """
          https://docs.idex.io/#get-candles
          [
              {
                  "start": 1590393000000,
                  "open": "202.11928302",
                  "high": "202.98100029",
                  "low": "201.85600392",
                  "close": "202.50192301",
                  "volume": "39.22576247",
                  "sequence": 848678
              },
              ...
          ]
        """
        pass

    async def get_trades(self):
        """
          https://docs.idex.io/#get-trades
          [
              {
                  "fillId": "a0b6a470-a6bf-11ea-90a3-8de307b3b6da",
                  "price": "202.74900000",
                  "quantity": "10.00000000",
                  "quoteQuantity": "2027.49000000",
                  "time": 1590394500000,
                  "makerSide": "sell",
                  "sequence": 848778
              },
              ...
          ]
        """
        pass

    async def get_order_book_l1(self):
        """
          https://docs.idex.io/#get-order-books

          [ price, quantity available, number of orders at price level ]

          {
              "sequence": 71228121,
              "bids": [
                  [ "202.00200000", "13.88204000", 2 ]
              ],
              "asks": [
                  [ "202.01000000", "8.11400000", 1 ]
              ]
          }
        """
        pass

    async def get_order_book_l2(self):
        """
          https://docs.idex.io/#get-order-books

          [ price, quantity available, number of orders at price level ]

          {
              "sequence": 71228121,
              "bids": [
                  [ "202.00200000", "13.88204000", 2 ],
                  [ "202.00100000", "10.00000000", 1 ],
                  ...
              ],
              "asks": [
                  [ "202.01000000", "8.11400000", 1 ],
                  [ "202.01200000", "21.50550000", 3 ],
                  ...
              ]
          }
        """
        pass
