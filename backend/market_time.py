"""
Class that handles the time framing of the market
Defines market time frame duration
Market time starts one time frame before the actual creation of the market in which we assume all drinks orders are equally in demand for the median price
 - name for initial default OrderRecord -> null_frame or null_record
Dictionary of OrderRecords

"""
from datetime import datetime, timedelta
from backend.orders import OrderRecord

class MarketTime:
        def __init__(self, frame_duration, market_instantiation_time, price_menu):
                self.frame_duration = frame_duration #seconds
                self.start_time =  market_instantiation_time
                self.frames = {}
                self.frames[-1] = self.construct_null_frame(price_menu)
        
        def construct_null_frame(self, price_menu):
                null_frame_start_time = self.start_time - timedelta(seconds=90)
                null_rec = OrderRecord(null_frame_start_time, self.start_time)
                
                for i, (item, price) in enumerate(price_menu.items()):
                        null_rec.create_order(item, i, null_frame_start_time, True, price, "Market")
                
                return null_rec



        
                