def require_wallet_signature(wrap):
    def check_for_private_key(self, *args, **kwargs):
        if not self.config.has_private_key:
            ## Throw Error?
            pass
        return wrap(self, *args, **kwargs)
    return check_for_private_key
  
def require_api_secret(wrap):
    def check_for_api_secret(self, *args, **kwargs):
        if not self.config.has_api_secret:
            ## Throw Error?
            pass
        return wrap(self, *args, **kwargs)
    return check_for_api_secret