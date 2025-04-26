import threading
import time
import logging

class ORBTrader:
    def __init__(self, api, instruments):
        self.api = api
        self.instruments = instruments
        self.opening_ranges = {}
        self.order_placed = {symbol: False for symbol in instruments}
        logging.basicConfig(filename='logs/bot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    def update_opening_ranges(self):
        for symbol in self.instruments:
            high, low = self.api.get_opening_range(symbol)
            self.opening_ranges[symbol] = (high, low)
            print(f"Opening Range for {symbol}: High={high}, Low={low}")  # Debug print for opening ranges

    def check_and_place_order(self, symbol):
        while not self.order_placed[symbol]:
            try:
                ltp_data = self.api.get_ltp([symbol])
                if symbol in ltp_data:
                    ltp = float(ltp_data[symbol])
                    opening_high, opening_low = self.opening_ranges[symbol]

                    print(f"Checking {symbol}: LTP={ltp}, High={opening_high}, Low={opening_low}")

                    # Allow a 0.0001 buffer for EUR/USD or 0.1 for USD/JPY
                    margin = 0.0001 if 'USD' in symbol else 0.1

                    # Check if LTP is significantly above opening high or below opening low
                    if ltp > opening_high + margin:
                        print(f"Placing Buy Order for {symbol} at LTP {ltp} - Condition met (LTP > High + margin)")
                        self.api.place_order(symbol, "buy")
                        self.order_placed[symbol] = True
                        logging.info(f"Buy Order Placed for {symbol} at LTP {ltp}")

                    elif ltp < opening_low - margin:
                        print(f"Placing Sell Order for {symbol} at LTP {ltp} - Condition met (LTP < Low - margin)")
                        self.api.place_order(symbol, "sell")
                        self.order_placed[symbol] = True
                        logging.info(f"Sell Order Placed for {symbol} at LTP {ltp}")
                    else:
                        print(f"No action for {symbol} as LTP is within the range")

                else:
                    print(f"LTP data not available for {symbol}")

            except Exception as e:
                print(f"Error fetching LTP or processing {symbol}: {e}")

            time.sleep(2)  # Wait for 2 seconds before checkingg again


    def start_trading(self):
        self.update_opening_ranges()
        threads = []
        for symbol in self.instruments:
            print(f"Starting thread for {symbol}")  # Debug log
            t = threading.Thread(target=self.check_and_place_order, args=(symbol,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
