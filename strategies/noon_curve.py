from config import account_A, trading_client_A, search_params
from alpaca.trading.requests import GetAssetsRequest, StopOrderRequest, OrderRequest, MarketOrderRequest, LimitOrderRequest, TakeProfitRequest, StopLossRequest, TrailingStopOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass
def run():
    """
    Purchase an asset with a trailing stop
    """
    symbol = "APPL"
    quantity = 1
    
    try:
        quantity = float(quantity) 
    except ValueError:
        raise ValueError("Quantity must be a valid number")
       
    order = trading_client_A.submit_order(MarketOrderRequest(
        symbol=symbol,
        qty=quantity,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY
    ))
    trailing_stop = trading_client_A.submit_order(TrailingStopOrderRequest(
        symbol=symbol,
        qty=quantity,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.DAY,
        trail_percent=0.01
    ))
    return "Trailing stop order submitted"
