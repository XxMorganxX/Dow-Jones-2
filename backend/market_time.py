"""
Class that handles the time framing of the market
Defines market time frame duration
Market time starts one time frame before the actual creation of the market in which we assume all drinks orders are equally in demand for the median price
 - name for initial default OrderRecord -> null_frame or null_record
Dictionary of OrderRecords

"""
from datetime import datetime, timedelta
from backend.orders import OrderRecord, Order
from lib.utils import write_json_safely
import json

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

        #Takes in json orders with the keys representing the
        #index of the orders and the orders are the values
        def process_orders(self, all_orders):
            for index, order in all_orders.items():
                    
                    dt_timestamp =  datetime.strptime(order["timestamp"], "%H:%M:%S %Y-%m-%d")

                    start_order_delta_time = (dt_timestamp - self.start_time).total_seconds()

                    frame_index = int(start_order_delta_time//self.frame_duration)

                    new_order = Order.convert_dict_to_order(order)

                    if frame_index >= 0:
                        self.frames.setdefault(frame_index, []).append(new_order)
            
        def write_orders_json(self):
            frames_for_json = {}
            for index, ord_rec in self.frames.items():
                for order in ord_rec:
                    
            write_json_safely("../sample_data/frames.json", frames_for_json)

        

        
                