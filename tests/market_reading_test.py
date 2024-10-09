import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.market import Market

menu_items_path = "../sample_data/menu_items.txt"

test_market = Market()

test_market.read_drink_options(menu_items_path)