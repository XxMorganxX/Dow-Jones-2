from datetime import datetime
from lib.utils import read_drink_options
from backend.market_time import MarketTime

class Market:
	def __init__(self):
		menu_items_path = "../sample_data/menu_items.txt"

		self.frame_duration = 90 #seconds

		self.start_time = datetime.now()

		self.menu_info = read_drink_options(menu_items_path)
		self.price_menu = self.set_initial_prices(self.menu_info)

		self.history = MarketTime(self.frame_duration, self.start_time, self.price_menu)
		print(self.history.frames[-1])

		print(self.__get_start_time_str())

		
	def set_initial_prices(self, menu_info):
		price_menu = {}

		for name, price_range in menu_info:
			p_low, p_high = price_range.split(",")
			p_median = float(p_low) + ((float(p_high) - float(p_low))/2)
			price_menu[name] = p_median

		return price_menu

	

	def __get_start_time_str(self):
		return self.start_time.strftime("%H:%M:%S %Y-%m-%d")

	
