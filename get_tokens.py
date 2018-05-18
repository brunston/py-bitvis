"""get_tokens

Spins up a server to get user tokens from Fitbit.
"""

try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    
    from fitbit.api import Fitbit
    
except ImportError:
    raise ImportError('py-bitvis requires flask, python-fitbit, pymongo')

client_tokens = []
try:
    with open('fitbit_client_tokens.pri') as f:
        client_tokens = [token.strip() for token in f.readlines()]
except FileNotFoundError:
    raise PyBitVisException('fitbit_clients_tokens.pri not found. Consult readme.')

class AuthenticationServer:
    def __init__(self,
                 fb_client_id,
                 fb_client_secret,
                 redirect_url='http://127.0.0.1:8080'):
        """Initialize an OAuth2 client using python-fitbit"""
        self.success = """<h1>Fitbit authentication Successful!</h1>"""

        self.fitbit = Fitbit(fb_client_id, fb_client_secret,
                             redirect_uri=redirect_url,
                             timeout=15)
    
class PyBitVisException(Exception):
    """py-bitvis exception"""