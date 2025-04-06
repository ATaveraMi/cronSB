import os
from dotenv import load_dotenv
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.live import StockDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass


load_dotenv()

API_KEY = os.getenv("API_KEY_J")
SECRET_KEY = os.getenv("SECRET_KEY_J")


search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)


stock_historical_data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
wss_client = StockDataStream(API_KEY, SECRET_KEY)
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
account = trading_client.get_account()
