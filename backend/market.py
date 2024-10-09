class Market:
	def __init__(self):
		menu_items_path = "../sample_data/menu_items.txt"


		self.menu_info = read_drink_options()
		self.price_menu = None



	def read_drink_options(self, menu_items_path):
		menu = []

		with open(menu_items_path, 'r') as f:
			for line in f:
				stripped_line = ''.join(line.split())
				drink_name, price_range = stripped_line.split(":")
				menu_entry = (drink_name, price_range)
				menu.append(menu_entry)
		
		return menu
		
	def set_inital_prices(self, menu_info):
		price_menu = {}

		for name, price_range in menu_info