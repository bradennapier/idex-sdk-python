from typing import  Literal, List, Union, TypedDict

# Todo figure out how to fix pylint for importing

from src.config import APIConfig
from src.async_request import IDEXAsyncRequest

class RestResponseAsset(TypedDict):
    name: str
    symbol: str
    contractAddress: str
    assetDecimals: int
    exchangeDecimals: Literal[8]

class RestResponseMarket(TypedDict):
    market: str
    status: Union[
        Literal["active"],
        Literal["inactive"],
        Literal["cancelsOnly"],
        Literal["limitMakerOnly"]
    ]
    baseAsset: str
    baseAssetPrecision: Literal[8]
    quoteAsset: str
    quoteAssetPrecision: Literal[8]


class RestResponseExchange(TypedDict):
    """
    Returns basic information about the exchange.

    ### References
    - https://docs.idex.io/#get-exchange
    
    ### Attributes
        `timeZone: str`:
            summary: 'Timezone pass of the exchange'
            example: 'UTC'
        `serverTime: int`:
            summary: 'Current server timestamp in milliseconds'
            example: 1596938576511
        `ethereumDepositContractAddress: str`:
            summary: 'Ethereum address of the exchange custody contract for deposits'
            example: '0x...'
        `ethUsdPrice: str`:
            summary: 'Current price of ETH in USD'
            example: '406.46'
        `gasPrice: str`
        `volume24hUsd: str`
        `makerFeeRate: str`
        `takerFeeRate: str`
        `makerTradeMinimum: str`
        `takerTradeMinimum: str`
        `withdrawalMinimum: str`
    """    
    timeZone: Literal['UTC']
    serverTime: int
    ethereumDepositContractAddress: str
    ethUsdPrice: str
    gasPrice: str
    volume24hUsd: str
    makerFeeRate: str
    takerFeeRate: str
    makerTradeMinimum: str
    takerTradeMinimum: str
    withdrawalMinimum: str


class RestResponseServerTime(TypedDict):
    """
    Response to the `time` request.
    
    ### References
    - https://docs.idex.io/#get-time
    
    ### Attributes
        `serverTime: int`:
            summary: 'The timestamp from the server in milliseconds'
    """  
    serverTime: int

class RestResponsePing(TypedDict):
    """
    Response to the `ping` request.
    
    ### References
    - https://docs.idex.io/#get-ping
    """    
    pass

class PublicClient():
    def __init__(self, config: APIConfig):
        print('config', config)
        self.config = config

    async def create(self):
        self.request = IDEXAsyncRequest()
        await self.request.create()

    async def get_ping(self) -> RestResponsePing:
        """
        get_ping [summary]
            Check for server liveness

        [extended_summary]
            https://docs.idex.io/#get-ping

        Returns:
            RestResponsePing: [description]
        """
        return {}

    async def get_server_time(self) -> RestResponseServerTime:
        """
          https://docs.idex.io/#get-time
          {
            "serverTime": 1590408000000
          }
        """
        pass

    async def get_exchange(self) -> RestResponseExchange:
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

    async def get_assets(self) -> List[RestResponseAsset]:
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

    async def get_markets(self) -> List[RestResponseMarket]:
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
