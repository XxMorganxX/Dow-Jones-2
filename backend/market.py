from datetime import datetime
from lib.utils import read_drink_options
from backend.market_time import MarketTime
from tests.generate_test_orders import generate_test_orders_func
import json

class Market:
    def __init__(self):
        menu_items_path = "../sample_data/menu_items.txt"
        test_items_path = "../sample_data/test_orders.json"

        self.frame_duration = 40 #seconds

        self.start_time = datetime.now()

        self.menu_info = read_drink_options(menu_items_path)
        self.price_menu = self.set_initial_prices(self.menu_info)

        self.history = MarketTime(self.frame_duration, self.start_time, self.price_menu)

        generate_test_orders_func(100, self.start_time, (self.frame_duration*10))

        self.read_test_orders(test_items_path)
        
        #self.history.write_orders_json()


    def set_initial_prices(self, menu_info):
        price_menu = {}

        for name, price_range in menu_info:
            p_low, p_high = price_range.split(",")
            p_median = float(p_low) + ((float(p_high) - float(p_low))/2)
            price_menu[name] = p_median

        return price_menu
    
    def read_test_orders(self, file_path):
        data = None
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file '{file_path}' contains invalid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        if data == None:
            raise "Error Reading File"
        else:
            self.history.process_orders(data)
    



    def __get_start_time_str(self):
        return self.start_time.strftime("%H:%M:%S %Y-%m-%d")

