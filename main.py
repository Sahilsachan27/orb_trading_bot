from oanda_api import OandaAPI
from orb_bot import ORBTrader

ACCESS_TOKEN = "69dcb5112002124a097b8311da5d65c7-b08d28f67ea5a70aeb58674ff20acd14"
ACCOUNT_ID = "101-001-31594929-001"
INSTRUMENTS = ['EUR_USD', 'USD_JPY', 'GBP_USD']

api = OandaAPI(ACCESS_TOKEN, ACCOUNT_ID)
ltp_data = api.get_ltp(INSTRUMENTS)

ltp_data = api.get_ltp(INSTRUMENTS)
print("Live LTPs:")
for symbol, price in ltp_data.items():
    print(f"{symbol}: {price}")

# Initialize Trader
trader = ORBTrader(api, INSTRUMENTS)

# Start trading
trader.start_trading()    

