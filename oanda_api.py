from oandapyV20.endpoints.accounts import AccountSummary
from oandapyV20.endpoints.instruments import InstrumentsCandles
import oandapyV20

class OandaAPI:
    def __init__(self, access_token, account_id):
        self.access_token = access_token
        self.account_id = account_id
        self.client = oandapyV20.API(access_token=self.access_token)
    
    def get_ltp(self, instruments):
        ltp_data = {}
        for instrument in instruments:
            params = {
                "granularity": "S5",  # Granularity for recent ticks
                "count": 1,
                "price": "M"
            }
            candles = InstrumentsCandles(instrument=instrument, params=params)
            self.client.request(candles)
            last_price = candles.response['candles'][0]['mid']['c']
            ltp_data[instrument] = last_price
        return ltp_data
    
    def get_opening_range(self, instrument, count=5):
        params = {
            "granularity": "M15",  # 15-minute candles
            "count": count,
            "price": "M"  # midpoint prices
        }
        candles = InstrumentsCandles(instrument=instrument, params=params)
        self.client.request(candles)

        highs = []
        lows = []

        for candle in candles.response['candles']:
            highs.append(float(candle['mid']['h']))
            lows.append(float(candle['mid']['l']))

        opening_high = max(highs)
        opening_low = min(lows)

        return opening_high, opening_low
