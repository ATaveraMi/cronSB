import os
from dotenv import load_dotenv
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.live import StockDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass


load_dotenv()

API_KEY_A = os.getenv("API_KEY_A")
SECRET_KEY_A = os.getenv("SECRET_KEY_A")

# Comenten los que no sean suyos, pero por favor pasenme sus keys para los cron jobs

# API_KEY_G = os.getenv("API_KEY_G")
# SECRET_KEY_G = os.getenv("SECRET_KEY_G")

# API_KEY_J = os.getenv("API_KEY_J")
# SECRET_KEY_J = os.getenv("SECRET_KEY_J")

search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)


stock_historical_data_client_A = StockHistoricalDataClient(API_KEY_A, SECRET_KEY_A)
wss_client_A = StockDataStream(API_KEY_A, SECRET_KEY_A)
trading_client_A = TradingClient(API_KEY_A, SECRET_KEY_A, paper=True)
account_A = trading_client_A.get_account()

# stock_historical_data_client_G = StockHistoricalDataClient(API_KEY_G, SECRET_KEY_G)
# wss_client_G = StockDataStream(API_KEY_G, SECRET_KEY_G)
# trading_client_G = TradingClient(API_KEY_G, SECRET_KEY_G, paper=True)
# account_G = trading_client_G.get_account()

# stock_historical_data_client_J = StockHistoricalDataClient(API_KEY_J, SECRET_KEY_J)
# wss_client_J = StockDataStream(API_KEY_J, SECRET_KEY_J)
# trading_client_J = TradingClient(API_KEY_J, SECRET_KEY_J, paper=True)
# account_J = trading_client_J.get_account()

