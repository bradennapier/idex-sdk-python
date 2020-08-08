import hmac
import hashlib
import uuid

# TODO Consider inheritance based on python convention?


class APIConfig():
    """
      Provides common configuration options for an API Client and a single wallet.
    """

    def __init__(self, *,
                 api_key=None,
                 api_secret=None,
                 wallet_address=None,
                 wallet_private_key=None,
                 solidityKeccak=None,
                 ethSignMessage=None) -> None:
        self._api_key = api_key
        self._wallet_address = wallet_address
        self.solidityKeccak = solidityKeccak

        self._headers = {
            'Accept': 'application/json',
            'User-Agent': '@idexio/idex-sdk-python'
        }

        if api_key != None:
            self._headers['IDEX-API-Key'] = api_key

        if api_secret != None:
            def get_hmac_signature(self, querystring):
                return hmac.new(secret,
                                querystring,
                                digestmod=hashlib.sha256).hexdigest()

                self.get_hmac_signature = get_hmac_signature

        if wallet_private_key != None:
            def sign_message(self, message):
                return ethSignMessage(
                    message,
                    private_key=wallet_private_key
                )

            self.sign_message = sign_message

    def get_nonce():
        return uuid.uuid1()

    def get_headers(self, querystring=None):
        headers = self._headers.copy()
        if querystring != None:
            headers['IDEX-HMAC-Signature'] = self.get_hmac_signature(
                querystring)

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
