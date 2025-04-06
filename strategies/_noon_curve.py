from config.configA import account, trading_client, search_params
from alpaca.trading.requests import GetAssetsRequest, StopOrderRequest, OrderRequest, MarketOrderRequest, LimitOrderRequest, TakeProfitRequest, StopLossRequest, TrailingStopOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass
def run():
    """
    Purchase an asset with a trailing stop
    """
    symbol = "TSLA"
    quantity = 1
       
    trailing_stop_order = trading_client.submit_order(TrailingStopOrderRequest(
            symbol=symbol,
            qty=quantity,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
            trail_percent=1.0,  # 📉 Venta si baja 10% desde máximo
            extended_hours=False
        ))
    return "Trailing stop order submitted"
