import hmac
import hashlib
import uuid

from typing import Optional

# TODO Consider inheritance based on python convention?


class APIConfig():
    """
      Provides common configuration options for an API Client and a single wallet.
    """

    has_private_key = False
    has_api_key = False
    has_api_secret = False

    def __init__(self, *,
                 api_key: Optional[str] = None,
                 api_secret: Optional[str] = None,
                 wallet_address: Optional[str] = None,
                 wallet_private_key: Optional[str] = None,
                 solidityKeccak=None,
                 # eth sign message
                 sign_message=None,
                 # override default nonce handling
                 get_nonce=None,         
                 sandbox: Optional[bool] = True) -> None:
        """
        
        ### References:
        - https://docs.idex.io/#authentication
        
        ### Arguments:
            `api_key: str | None = None`:
                summary: 'Description here'
            `api_secret: str | None = None`
                summary: 'Description here'
            `wallet_address: str | None = None`: 
                summary: ''
            `wallet_private_key (Optional[str], optional)`: [description]. Defaults to None.
            `solidityKeccak ([type], optional)`: [description]. Defaults to None.
            `sign_message ([type], optional)`: [description]. Defaults to None.
            `get_nonce ([type], optional)`: [description]. Defaults to None.
            `sandbox (bool, optional)`: [description]. Defaults to True.

        ### Returns:
            [type]: [description]
        """        
        self._api_key = api_key
        self.wallet_address = wallet_address
        self.solidityKeccak = solidityKeccak
        self.sandbox = sandbox
        self._headers = {
            'Accept': 'application/json',
            'User-Agent': '@idexio/idex-sdk-python'
        }

        if get_nonce:
            self.get_nonce = get_nonce

        if api_key:
            self.has_api_key = True
            self._headers['IDEX-API-Key'] = api_key

        if api_secret:
            self.has_api_secret = True

            def get_hmac_signature(self: APIConfig, querystring: str) -> str:
                return hmac.new(api_secret,
                                querystring,
                                digestmod=hashlib.sha256).hexdigest()

            self.get_hmac_signature = get_hmac_signature

        if wallet_private_key:
            self.has_private_key = True

            def config_sign_message(self: APIConfig, message: str) -> str:
                return sign_message(
                    message,
                    private_key=wallet_private_key
                )

            self.sign_message = config_sign_message

    def get_nonce(self):
        return uuid.uuid1()

    def get_rest_url(self):
        if self.sandbox == False:
            return 'https://api.idex.io/v1'
        else:
            return 'https://api-sandbox.idex.io/v1'

    def get_ws_url(self):
        if self.sandbox == False:
            return 'wss://websocket.idex.io/v1'
        else:
            return 'wss://websocket-sandbox.idex.io/v1'

    def get_headers(self, querystring: Optional[str] = None):
        headers = self._headers.copy()
        # TODO - Handle when dont have private key (get_hmac_signature wont be defined)
        if querystring and self.get_hmac_signature:
            headers['IDEX-HMAC-Signature'] = self.get_hmac_signature(
                querystring=querystring
            )

        return headers

    def get_order_signature(self, d):
        return self.solidityKeccak(
            ['uint128', 'uint128', 'string', 'string'],
            [d['nonce'], d['wallet'], d['orderId'], d['market']]
        )

    def get_cancel_signature(self, d):
        data = d.copy()
        data.setdefault('orderId', '')
        data.setdefault('market', '')
        return self.solidityKeccak(
            ['uint128', 'address', 'string', 'string'],
            [data['nonce'], data['wallet'], data['orderId'], data['market']]
        )

    def get_withdrawal_signature(self, d):
        # TODO Handle asset vs assetContractAddress
        return self.solidityKeccak(
            ['uint128', 'address', 'string', 'string', 'bool'],
            [d['nonce'], d['wallet'], d['asset'], d['quantity'], True]
        )

    def get_associate_wallet_signature(self, d):
        return self.solidityKeccak(
            ['uint128', 'address'],
            [d['nonce'], d['wallet']]
        )
